import asyncio

import httpx

from business_central_tool.app.core.config import settings


RETRYABLE_STATUS_CODES = {
    429,
    500,
    502,
    503,
    504,
}


async def sleep_before_retry(attempt: int) -> None:
    delay = min(
        2**attempt,
        settings.max_retry_delay,
    )

    await asyncio.sleep(delay)


def is_retryable_status(status_code: int) -> bool:
    return status_code in RETRYABLE_STATUS_CODES


def is_retryable_exception(exc: Exception) -> bool:
    return isinstance(
        exc,
        (
            httpx.ConnectError,
            httpx.ReadTimeout,
            httpx.WriteTimeout,
            httpx.PoolTimeout,
        ),
    )