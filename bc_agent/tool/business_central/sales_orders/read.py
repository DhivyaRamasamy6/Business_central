from agent_framework import tool
import httpx
import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL=os.getenv("HTTP_BASE_URL")


@tool(
    name="list_sales_orders",
    description="""
    List Business Central sales orders.

    Use when the user wants multiple sales orders or wants to
    retrieve orders using supported criteria such as customer,
    status, or date range.

    Operation: READ.
    """,
    approval_mode="never_require"
)
async def list_sales_order(company_id:str):
    async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{BASE_URL}/api/business-central/companies/{company_id}/sales-orders"
                )
         
                response.raise_for_status()
                return response.json()

    

@tool(
    name="get_sales_order",
    description="""
    Retrieve one specific Business Central sales order.

    Use when the user wants details about one sales order
    and provides the exact sales order ID.

    Do not use for searching when the exact ID is unknown.

    Operation: READ.

    """,
    approval_mode="never_require"
)
async def get_sales_order(company_id:str,sales_order_id:str):
    async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{BASE_URL}/api/business-central/companies/{company_id}/sales-orders/{sales_order_id}"
                )
         
                response.raise_for_status()
                return response.json()