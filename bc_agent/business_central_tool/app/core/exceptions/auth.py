from .base import BusinessCentralError


class AuthenticationError(BusinessCentralError):
    """Raised when authentication fails."""


class TokenExpiredError(BusinessCentralError):
    """Raised when an access token has expired."""


class TokenRefreshError(BusinessCentralError):
    """Raised when an access token cannot be refreshed."""


class AuthorizationError(BusinessCentralError):
    """Raised when the API returns HTTP 403 Forbidden."""