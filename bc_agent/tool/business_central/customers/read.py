from agent_framework import tool
import httpx
import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL=os.getenv("HTTP_BASE_URL")


@tool(
    name="list_customers",
    description="""
    List Business Central customers for a company.

    Use when the user wants multiple customers or a general
    customer list.

    Do not use when the user wants one specific customer
    and already has the exact customer ID.

    Operation: READ.
    """,
    approval_mode="never_require"
    )
async def list_customers(company_id:str):
    async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/api/business-central/companies/{company_id}/customers"
            )
     
            response.raise_for_status()
            return response.json()


@tool(
        name="get_customer",
        description="""
        Retrieve one specific Business Central customer.

        Use when:
        - The user wants details about one customer.
        - The user provides the exact customer ID.

        Do not use when the user only provides a name, email,
        or customer number and needs to find the customer.

        Operation: READ.
        """,
        approval_mode="never_require"
    )
async def get_customer(company_id:str,customer_id:str):
    async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/api/business-central/companies/{company_id}/customers/{customer_id}"
            )
     
            response.raise_for_status()
            return response.json()
