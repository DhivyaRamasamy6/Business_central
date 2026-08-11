from .base import BusinessCentralError


class BadRequestError(BusinessCentralError):
    """HTTP 400."""


class ResourceNotFoundError(BusinessCentralError):
    """HTTP 404."""


class ConflictError(BusinessCentralError):
    """HTTP 409."""


class RateLimitError(BusinessCentralError):
    """HTTP 429."""


class BusinessCentralAPIError(BusinessCentralError):
    """Generic Business Central API error."""