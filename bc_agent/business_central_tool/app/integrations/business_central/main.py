from typing import Any
import asyncio
import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP

PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

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
from business_central_tool.app.integrations.business_central.tools.company_tools import (
    get_companies,
    validate_company,
)
from business_central_tool.app.integrations.business_central.tools.customer_tools import (
    get_customer,
    list_customers,
)


# ============================================================
# MCP SERVER
# ============================================================

mcp = FastMCP(
    name="Business Central MCP Server",
    instructions=(
        "MCP server providing read-only access to "
        "Microsoft Dynamics 365 Business Central."
    ),
)


# ============================================================
# SHARED DEPENDENCIES
# ============================================================

token_cache = TokenCache()

token_manager = TokenManager(
    cache=token_cache,
)

auth_service = AuthenticationService(
    token_manager=token_manager,
)

business_central_client = BusinessCentralClient(
    auth_service=auth_service,
)

company_service = CompanyService(
    client=business_central_client,
)

customer_service = CustomerService(
    client=business_central_client,
)


# ============================================================
# COMPANY READ TOOLS
# ============================================================


@mcp.tool(
    name="get_companies",
    description=(
        "Retrieve all companies available in "
        "Microsoft Dynamics 365 Business Central."
    ),
)
async def get_companies_tool() -> list[dict[str, Any]]:
    """
    Retrieve all Business Central companies.
    """

    return await get_companies(
        company_service=company_service,
    )


@mcp.tool(
    name="validate_company",
    description=(
        "Validate that a Business Central company exists "
        "using its company ID."
    ),
)
async def validate_company_tool(
    company_id: str,
) -> dict[str, Any]:
    """
    Validate a Business Central company.
    """

    return await validate_company(
        company_service=company_service,
        company_id=company_id,
    )


# ============================================================
# CUSTOMER READ TOOLS
# ============================================================


@mcp.tool(
    name="list_customers",
    description=(
        "Retrieve customers from a Business Central company."
    ),
)
async def list_customers_tool(
    company_id: str,
    top: int = 100,
    skip: int = 0,
) -> list[dict[str, Any]]:
    """
    Retrieve customers from a Business Central company.

    Args:
        company_id:
            Business Central company UUID.

        top:
            Maximum number of customers to return.

        skip:
            Number of customers to skip.
    """

    customers = await list_customers(
        customer_service=customer_service,
        company_id=company_id,
        top=top,
        skip=skip,
    )

    return [
        customer.model_dump(mode="json")
        for customer in customers
    ]


@mcp.tool(
    name="get_customer",
    description=(
        "Retrieve a single customer from "
        "a Business Central company."
    ),
)
async def get_customer_tool(
    company_id: str,
    customer_id: str,
) -> dict[str, Any]:
    """
    Retrieve a single Business Central customer.

    Args:
        company_id:
            Business Central company UUID.

        customer_id:
            Business Central customer UUID.
    """

    customer = await get_customer(
        customer_service=customer_service,
        company_id=company_id,
        customer_id=customer_id,
    )

    return customer.model_dump(mode="json")


# ============================================================
# SERVER ENTRY POINT
# ============================================================


if __name__ == "__main__":
    asyncio.run(mcp.run_stdio_async())