from .base import BusinessCentralError


class InvalidTenantError(BusinessCentralError):
    """Invalid tenant ID."""


class InvalidEnvironmentError(BusinessCentralError):
    """Invalid environment."""


class InvalidCompanyError(BusinessCentralError):
    """Invalid company ID."""


class InvalidResourceIdError(BusinessCentralError):
    """Invalid resource ID."""