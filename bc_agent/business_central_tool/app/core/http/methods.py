from typing import Any

import httpx

from business_central_tool.app.core.http.client import HTTPClient
from business_central_tool.app.core.logging import setup_logger

logger = setup_logger(__name__)


class HTTPMethods:

    @staticmethod
    async def get(
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
    ) -> httpx.Response:

        logger.info(f"GET {url}")

        client = HTTPClient.get_client()

        return await client.get(
            url=url,
            headers=headers,
            params=params,
        )

    @staticmethod
    async def post(
        url: str,
        headers: dict | None = None,
        json: dict | None = None,
        data: Any = None,
    ) -> httpx.Response:

        logger.info(f"POST {url}")

        client = HTTPClient.get_client()

        return await client.post(
            url=url,
            headers=headers,
            json=json,
            data=data,
        )

    @staticmethod
    async def patch(
        url: str,
        headers: dict | None = None,
        json: dict | None = None,
    ) -> httpx.Response:

        logger.info(f"PATCH {url}")

        client = HTTPClient.get_client()

        return await client.patch(
            url=url,
            headers=headers,
            json=json,
        )

    @staticmethod
    async def delete(
        url: str,
        headers: dict | None = None,
    ) -> httpx.Response:

        logger.info(f"DELETE {url}")

        client = HTTPClient.get_client()

        return await client.delete(
            url=url,
            headers=headers,
        )