from fastapi import FastAPI

from business_central_tool.app.api.business_central.company_router import (
    router as company_router,
)
from business_central_tool.app.api.business_central.customer_router import (
    router as customer_router,
)
from business_central_tool.app.api.business_central.invoice_router import (
    router as invoice_router,
)
from business_central_tool.app.api.business_central.sales_order_router import (
    router as sales_order_router,
)

from business_central_tool.app.core.exceptions.auth import (
    AuthenticationError,
    AuthorizationError,
    TokenExpiredError,
    TokenRefreshError,
)
from business_central_tool.app.core.exceptions.base import (
    BusinessCentralError,
)
from business_central_tool.app.core.exceptions.business_central import (
    BadRequestError,
    BusinessCentralAPIError,
    ConflictError,
    RateLimitError,
    ResourceNotFoundError,
)
from business_central_tool.app.core.exceptions.handlers import (
    authentication_error_handler,
    authorization_error_handler,
    bad_request_error_handler,
    business_central_api_error_handler,
    business_central_error_handler,
    conflict_error_handler,
    rate_limit_error_handler,
    resource_not_found_error_handler,
    token_expired_error_handler,
    token_refresh_error_handler,
)
from api.router import router as agent_router

app = FastAPI(
    title="Business Central Backend API",
    description=(
        "Enterprise REST API for Business Central integrations."
    ),
    version="1.0.0",
)


# ============================================================
# EXCEPTION HANDLERS
# ============================================================

app.add_exception_handler(
    AuthenticationError,
    authentication_error_handler,
)

app.add_exception_handler(
    AuthorizationError,
    authorization_error_handler,
)

app.add_exception_handler(
    BadRequestError,
    bad_request_error_handler,
)

app.add_exception_handler(
    ResourceNotFoundError,
    resource_not_found_error_handler,
)

app.add_exception_handler(
    ConflictError,
    conflict_error_handler,
)

app.add_exception_handler(
    RateLimitError,
    rate_limit_error_handler,
)

app.add_exception_handler(
    TokenExpiredError,
    token_expired_error_handler,
)

app.add_exception_handler(
    TokenRefreshError,
    token_refresh_error_handler,
)

app.add_exception_handler(
    BusinessCentralAPIError,
    business_central_api_error_handler,
)

app.add_exception_handler(
    BusinessCentralError,
    business_central_error_handler,
)


# ============================================================
# BUSINESS CENTRAL REST API ROUTERS
# ============================================================
app.include_router(agent_router)
app.include_router(company_router)

app.include_router(customer_router)

app.include_router(invoice_router)

app.include_router(sales_order_router)