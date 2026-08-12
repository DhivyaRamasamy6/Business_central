from agent_framework import tool
import httpx
import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL=os.getenv("HTTP_BASE_URL")


@tool(
    name="list_sales_invoices",
    description="""
    List Business Central sales invoices.

    Use when the user wants multiple invoices or wants to retrieve
    invoices using supported criteria such as customer, status,
    or date range.

    Operation: READ.
    """,
    approval_mode="never_require"
)
async def list_invoices(company_id:str):
    async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/api/business-central/companies/{company_id}/invoices"
            )
     
            response.raise_for_status()
            return response.json()


@tool(
    name="get_sales_invoice",
    description="""
    Retrieve one specific Business Central sales invoice.

    Use when the user wants details about one sales invoice
    and provides the exact invoice ID.

    Do not use for searching when the exact ID is unknown.

    Operation: READ.
    """,
    approval_mode="never_require"
)
async def get_invoice(company_id:str,invoice_id:str):
      async with httpx.AsyncClient() as client:
                  response = await client.get(
                      f"{BASE_URL}/api/business-central/companies/{company_id}/invoices/{invoice_id}"
                  )
           
                  response.raise_for_status()
                  return response.json()