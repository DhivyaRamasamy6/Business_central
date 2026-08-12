from functools import lru_cache

from business_central_tool.app.integrations.business_central.auth.auth_service import (
    AuthenticationService,
)
from business_central_tool.app.integrations.business_central.auth.token_cache import (
    TokenCache,
)
from business_central_tool.app.integrations.business_central.auth.token_manager import (
    TokenManager,
)
from business_central_tool.app.integrations.business_central.client.business_central_client import (
    BusinessCentralClient,
)
from business_central_tool.app.integrations.business_central.services.company_service import (
    CompanyService,
)
from business_central_tool.app.integrations.business_central.services.customer_service import (
    CustomerService,
)
from business_central_tool.app.integrations.business_central.services.invoice_service import (
    InvoiceService,
)
from business_central_tool.app.integrations.business_central.services.sales_order_service import (
    SalesOrderService,
)


@lru_cache
def get_token_cache() -> TokenCache:
    """
    Return the application-level Business Central token cache.

    A single cache instance is shared by the application so that
    access tokens are reused between requests.
    """
    return TokenCache()


@lru_cache
def get_token_manager() -> TokenManager:
    """
    Return the application-level token manager.
    """
    return TokenManager(
        cache=get_token_cache(),
    )


@lru_cache
def get_authentication_service() -> AuthenticationService:
    """
    Return the application-level Business Central authentication service.
    """
    return AuthenticationService(
        token_manager=get_token_manager(),
    )


@lru_cache
def get_business_central_client() -> BusinessCentralClient:
    """
    Return the application-level Business Central HTTP client.

    The client is responsible for:
    - authentication
    - token refresh
    - headers
    - retries
    - correlation IDs
    - HTTP error mapping
    """
    return BusinessCentralClient(
        auth_service=get_authentication_service(),
    )


@lru_cache
def get_company_service() -> CompanyService:
    """
    Return the application-level Company service.
    """
    return CompanyService(
        client=get_business_central_client(),
    )


@lru_cache
def get_customer_service() -> CustomerService:
    """
    Return the application-level Customer service.
    """
    return CustomerService(
        client=get_business_central_client(),
    )

@lru_cache
def get_invoice_service() -> InvoiceService:
    """
    Return the application-level Invoice service.
    """
    return InvoiceService(
        client=get_business_central_client(),
    )

@lru_cache
def get_sales_order_service() -> SalesOrderService:
    """
    Return the application-level Sales Order service.
    """

    return SalesOrderService(
        client=get_business_central_client(),
    )