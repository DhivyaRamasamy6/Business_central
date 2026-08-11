import uuid
from typing import Any

import httpx

from business_central_tool.app.core.exceptions import (
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    BusinessCentralAPIError,
    ConflictError,
    RateLimitError,
    ResourceNotFoundError,
)
from business_central_tool.app.core.logging import setup_logger
from business_central_tool.app.core.retry.policy import (
    is_retryable_exception,
    is_retryable_status,
    sleep_before_retry,
)
from business_central_tool.app.core.http import HTTPClient

from ..auth.auth_service import AuthenticationService
from .headers import HeaderBuilder

logger = setup_logger(__name__)


class BusinessCentralClient:
    """
    Facade over Business Central HTTP APIs.

    Responsibilities:
    - Authentication
    - Header construction
    - Correlation IDs
    - Retry handling
    - 401 token refresh
    - HTTP status mapping
    """

    def __init__(
        self,
        auth_service: AuthenticationService,
    ) -> None:
        self._auth_service = auth_service

    async def get(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        return await self._request(
            method="GET",
            url=url,
            params=params,
        )

    async def post(
        self,
        url: str,
        *,
        payload: dict[str, Any],
    ) -> dict[str, Any]:

        return await self._request(
            method="POST",
            url=url,
            json=payload,
        )

    async def patch(
        self,
        url: str,
        *,
        payload: dict[str, Any],
        etag: str | None = None,
    ) -> dict[str, Any]:

        headers_extra = {}

        if etag:
            headers_extra["If-Match"] = etag

        return await self._request(
            method="PATCH",
            url=url,
            json=payload,
            headers_extra=headers_extra,
        )

    async def delete(
        self,
        url: str,
        *,
        etag: str | None = None,
    ) -> None:

        headers_extra = {}

        if etag:
            headers_extra["If-Match"] = etag

        await self._request(
            method="DELETE",
            url=url,
            headers_extra=headers_extra,
        )

    async def _request(
        self,
        *,
        method: str,
        url: str,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        headers_extra: dict[str, str] | None = None,
    ) -> dict[str, Any]:

        correlation_id = str(uuid.uuid4())

        auth_retry_used = False
        retry_attempt = 0

        while True:
            token = await self._auth_service.get_access_token()

            headers = HeaderBuilder.json(token)

            if method == "GET":
                headers.pop("Content-Type", None)

            if headers_extra:
                headers.update(headers_extra)

            logger.info(
                "[%s] %s %s",
                correlation_id,
                method,
                url,
            )

            try:

                response = await self._send(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    json=json,
                )
                

            except Exception as exc:
                if (
                    is_retryable_exception(exc)
                    and retry_attempt < 3
                ):
                    await sleep_before_retry(retry_attempt)
                    retry_attempt += 1
                    continue

                raise

            logger.info(
                "[%s] HTTP %s",
                correlation_id,
                response.status_code,
            )

            # -----------------------------------------
            # 401 → refresh token exactly once
            # -----------------------------------------

            if response.status_code == 401:
                if auth_retry_used:
                    raise AuthenticationError(
                        "Business Central rejected the refreshed token.",
                        status_code=401,
                        correlation_id=correlation_id,
                    )

                auth_retry_used = True

                logger.warning(
                    "[%s] Received 401. Refreshing token.",
                    correlation_id,
                )

                await self._auth_service.force_refresh()

                continue

            # -----------------------------------------
            # Retryable HTTP errors
            # -----------------------------------------

            if is_retryable_status(response.status_code):
                if retry_attempt < 3:
                    await sleep_before_retry(retry_attempt)
                    retry_attempt += 1
                    continue

            return self._process_response(
                response,
                correlation_id,
            )

    async def _send(
        self,
        *,
        method: str,
        url: str,
        headers: dict[str, str],
        params: dict[str, Any] | None,
        json: dict[str, Any] | None,
    ) -> httpx.Response:

        if method == "GET":
            return await HTTPClient.get(
                url,
                headers=headers,
                params=params,
            )

        if method == "POST":
            return await HTTPClient.post(
                url,
                headers=headers,
                json=json,
            )

        if method == "PATCH":
            return await HTTPClient.patch(
                url,
                headers=headers,
                json=json,
            )

        if method == "DELETE":
            return await HTTPClient.delete(
                url,
                headers=headers,
            )

        raise ValueError(f"Unsupported HTTP method: {method}")

    @staticmethod
    def _process_response(
        response: httpx.Response,
        correlation_id: str,
    ) -> dict[str, Any]:

        status = response.status_code

        if status in (200, 201):
            return response.json()

        if status == 204:
            return {}

        message = response.text

        if status == 400:
            raise BadRequestError(
                message,
                status_code=status,
                correlation_id=correlation_id,
            )

        if status == 403:
            raise AuthorizationError(
                message,
                status_code=status,
                correlation_id=correlation_id,
            )

        if status == 404:
            raise ResourceNotFoundError(
                message,
                status_code=status,
                correlation_id=correlation_id,
            )

        if status == 409:
            raise ConflictError(
                message,
                status_code=status,
                correlation_id=correlation_id,
            )

        if status == 429:
            raise RateLimitError(
                message,
                status_code=status,
                correlation_id=correlation_id,
            )

        raise BusinessCentralAPIError(
            message,
            status_code=status,
            correlation_id=correlation_id,
        )