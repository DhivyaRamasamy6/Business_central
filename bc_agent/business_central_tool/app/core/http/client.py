from typing import Any

import httpx

from business_central_tool.app.core.config import settings


class HTTPClient:
    """
    Centralized asynchronous HTTP client.

    Provides connection pooling and common HTTP operations.
    """

    _client: httpx.AsyncClient | None = None

    @classmethod
    def get_client(cls) -> httpx.AsyncClient:
        if cls._client is None:
            timeout = httpx.Timeout(
                connect=10.0,
                read=settings.http_timeout,
                write=settings.http_timeout,
                pool=10.0,
            )

            cls._client = httpx.AsyncClient(
                timeout=timeout,
                follow_redirects=True,
            )

        return cls._client

    @classmethod
    async def get(
        cls,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        params: dict[str, Any] | None = None,
    ) -> httpx.Response:
        client = cls.get_client()

        return await client.get(
            url,
            headers=headers,
            params=params,
        )

    @classmethod
    async def post(
        cls,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        json: Any = None,
    ) -> httpx.Response:
        client = cls.get_client()

        return await client.post(
            url,
            headers=headers,
            json=json,
        )

    @classmethod
    async def post_form(
        cls,
        url: str,
        *,
        data: dict[str, Any],
    ) -> httpx.Response:
        client = cls.get_client()

        return await client.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
        )

    @classmethod
    async def patch(
        cls,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        json: Any = None,
    ) -> httpx.Response:
        client = cls.get_client()

        return await client.patch(
            url,
            headers=headers,
            json=json,
        )

    @classmethod
    async def delete(
        cls,
        url: str,
        *,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        client = cls.get_client()

        return await client.delete(
            url,
            headers=headers,
        )

    @classmethod
    async def close(cls) -> None:
        if cls._client:
            await cls._client.aclose()
            cls._client = None