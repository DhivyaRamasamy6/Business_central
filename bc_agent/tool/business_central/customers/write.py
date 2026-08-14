from agent_framework import tool
import httpx
import os
from business_central_tool.app.integrations.business_central.schemas.customer import CustomerCreateRequest,CustomerUpdateRequest
from dotenv import load_dotenv
load_dotenv()
BASE_URL=os.getenv("HTTP_BASE_URL")
@tool(
    name="create_customer",
    description="""
    Create a new Business Central customer.

    USE WHEN:
    - The user explicitly asks to create, add, or register a new customer.

    DO NOT USE WHEN:
    - The user asks to retrieve or list customers.
    - The user asks to modify an existing customer.
    - The user asks to delete a customer.

    REQUIRED:
    - company_id: valid Business Central company UUID
    - customer.displayName: 1-100 characters

    OPTIONAL:
    - customer.type
    - customer.addressLine1
    - customer.addressLine2
    - customer.city
    - customer.state
    - customer.country
    - customer.postalCode
    - customer.phoneNumber
    - customer.email
    - customer.website

    Do not invent missing values.
    Do not require customer_id for creation.

    OPERATION: WRITE.
""",
    
    approval_mode="always_require",
)
async def create_customer(
    company_id: str,
    customer: CustomerCreateRequest|dict,
):
    if isinstance(customer, dict):
        customer = CustomerCreateRequest.model_validate(customer)
 
    url = (
        f"{BASE_URL}/api/business-central/"
        f"companies/{company_id}/customers"
    )

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            json=customer.model_dump(exclude_none=True),
        )

        response.raise_for_status()
        return response.json()


@tool(
    name="update_customer",
    description="""
   Update an existing Business Central customer.

    USE WHEN:
    - The user explicitly asks to change, modify, edit, or update an existing customer.

    DO NOT USE WHEN:
    - The user asks to create a new customer.
    - The user asks to retrieve customer information.
    - The user asks to delete a customer.

    REQUIRED:
    - company_id: valid UUID
    - customer_id: valid UUID
    - customer: fields to update
    - etag: current customer ETag

    Do not invent customer_id or ETag.

    OPERATION: WRITE.

""",
    approval_mode="always_require",
)
async def update_customer(company_id: str,customer_id: str,customer: CustomerUpdateRequest,etag: str):
    if isinstance(customer, dict):
            customer = CustomerUpdateRequest.model_validate(customer)
     
    async with httpx.AsyncClient() as client:
        url=f"{BASE_URL}/api/business-central/companies/{company_id}/customers/{customer_id}"
        response = await client.patch(
            url,
            params={"etag": etag,},
            json=customer.model_dump_json(exclude_none=True),
        )
    
        response.raise_for_status()
        return response.json()
    

@tool(
    name="delete_customer",
    description="""
    Delete an existing Business Central customer.

    Use only when the user explicitly requests deletion.

    This is a destructive operation.

    Operation: WRITE.
""",
    
    approval_mode="always_require",
)


async def delete_customer(company_id: str, customer_id: str, etag: str):
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/api/business-central/companies/{company_id}/customers/{customer_id}"
        response = await client.delete(
            url,
            params={"etag": etag},
        )
        response.raise_for_status()

        if response.status_code == 204 or not response.content:
            return {"status": "deleted", "customer_id": customer_id}

        return response.json()

