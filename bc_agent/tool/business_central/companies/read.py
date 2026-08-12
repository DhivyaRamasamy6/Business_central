from agent_framework import tool
import httpx
import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL=os.getenv("HTTP_BASE_URL")

@tool(name="list_companies",
      description="""
    List all Business Central companies available to the authenticated user.
    Use for company discovery and retrieval.
    Operation: READ
    """,
    approval_mode="never_require") 
async def list_companies():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/api/business-central/companies"
        )
 
        response.raise_for_status()
        return response.json()



@tool(
    name="get_company",
    description="""
    Retrieve a specific Business Central company by its exact company ID.

    Use when the user provides a company ID.
    Operation: READ.
    """,
    approval_mode="always_require"
)
async def get_company(comapany_id:str):
    async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/api/business-central/companies/{comapany_id}"
            )
     
            response.raise_for_status()
            return response.json()
    