from business_central_tool.app.core.config import settings


class CredentialProvider:
    """
    Provides Business Central authentication credentials.

    The rest of the application must not directly access
    the client secret from configuration.
    """

    @staticmethod
    def get_tenant_id() -> str:
        return settings.bc_tenant_id

    @staticmethod
    def get_client_id() -> str:
        return settings.bc_client_id

    @staticmethod
    def get_client_secret() -> str:
        return settings.bc_client_secret