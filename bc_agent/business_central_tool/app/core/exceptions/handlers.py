import json
import logging
from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse

from .auth import (
    AuthenticationError,
    AuthorizationError,
    TokenExpiredError,
    TokenRefreshError,
)

from .base import BusinessCentralError

from .business_central import (
    BadRequestError,
    BusinessCentralAPIError,
    ConflictError,
    RateLimitError,
    ResourceNotFoundError,
)

logger = logging.getLogger(__name__)


def _extract_error_message(exc: Exception) -> str:
    """
    Extract a clean Business Central error message.

    Business Central commonly returns:

    {
        "error": {
            "code": "...",
            "message": "..."
        }
    }
    """

    raw_message = str(exc)

    try:
        data = json.loads(raw_message)

        error = data.get("error")

        if isinstance(error, dict):
            message = error.get("message")

            if message:
                return message

    except (json.JSONDecodeError, TypeError):
        pass

    return raw_message


def _error_response(
    *,
    status_code: int,
    error: str,
    message: str,
) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "error": error,
            "message": message,
        },
    )


async def authentication_error_handler(
    request: Request,
    exc: AuthenticationError,
) -> JSONResponse:

    logger.error(
        "Business Central authentication error: %s",
        exc,
    )

    return _error_response(
        status_code=401,
        error="authentication_error",
        message=_extract_error_message(exc),
    )


async def authorization_error_handler(
    request: Request,
    exc: AuthorizationError,
) -> JSONResponse:

    logger.warning(
        "Business Central authorization error: %s",
        exc,
    )

    return _error_response(
        status_code=403,
        error="authorization_error",
        message=_extract_error_message(exc),
    )


async def bad_request_error_handler(
    request: Request,
    exc: BadRequestError,
) -> JSONResponse:

    logger.warning(
        "Business Central bad request: %s",
        exc,
    )

    return _error_response(
        status_code=400,
        error="bad_request",
        message=_extract_error_message(exc),
    )


async def resource_not_found_error_handler(
    request: Request,
    exc: ResourceNotFoundError,
) -> JSONResponse:

    logger.info(
        "Business Central resource not found: %s",
        exc,
    )

    return _error_response(
        status_code=404,
        error="resource_not_found",
        message=_extract_error_message(exc),
    )


async def conflict_error_handler(
    request: Request,
    exc: ConflictError,
) -> JSONResponse:

    logger.warning(
        "Business Central resource conflict: %s",
        exc,
    )

    return _error_response(
        status_code=409,
        error="conflict",
        message=_extract_error_message(exc),
    )


async def rate_limit_error_handler(
    request: Request,
    exc: RateLimitError,
) -> JSONResponse:

    logger.warning(
        "Business Central rate limit: %s",
        exc,
    )

    return _error_response(
        status_code=429,
        error="rate_limit",
        message=_extract_error_message(exc),
    )


async def token_expired_error_handler(
    request: Request,
    exc: TokenExpiredError,
) -> JSONResponse:

    logger.warning(
        "Business Central token expired: %s",
        exc,
    )

    return _error_response(
        status_code=401,
        error="token_expired",
        message=_extract_error_message(exc),
    )


async def token_refresh_error_handler(
    request: Request,
    exc: TokenRefreshError,
) -> JSONResponse:

    logger.error(
        "Business Central token refresh failed: %s",
        exc,
    )

    return _error_response(
        status_code=401,
        error="token_refresh_error",
        message=_extract_error_message(exc),
    )


async def business_central_api_error_handler(
    request: Request,
    exc: BusinessCentralAPIError,
) -> JSONResponse:

    logger.error(
        "Business Central API error: %s",
        exc,
    )

    return _error_response(
        status_code=502,
        error="business_central_api_error",
        message=_extract_error_message(exc),
    )


async def business_central_error_handler(
    request: Request,
    exc: BusinessCentralError,
) -> JSONResponse:

    logger.error(
        "Business Central error: %s",
        exc,
    )

    return _error_response(
        status_code=500,
        error="business_central_error",
        message=_extract_error_message(exc),
    )