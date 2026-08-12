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

from api.router import router as agent_router
app = FastAPI(
    title="Business Central Backend API",
    description=(
        "Enterprise REST API for Business Central integrations."
    ),
    version="1.0.0",
)

app.include_router(agent_router)
app.include_router(company_router)
app.include_router(customer_router)
app.include_router(invoice_router)
app.include_router(sales_order_router)