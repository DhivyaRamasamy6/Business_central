from .auth.auth_service import AuthenticationService
from .auth.token_cache import TokenCache
from .auth.token_manager import TokenManager
from .client.business_central_client import BusinessCentralClient
from .services.company_service import CompanyService
from .services.customer_service import CustomerService


def create_business_central_services():
    token_cache = TokenCache()

    token_manager = TokenManager(
        cache=token_cache
    )

    auth_service = AuthenticationService(
        token_manager=token_manager
    )

    client = BusinessCentralClient(
        auth_service=auth_service
    )

    return {
        "auth": auth_service,
        "client": client,
        "companies": CompanyService(client),
        "customers": CustomerService(client),
    }


__all__ = [
    "create_business_central_services",
]