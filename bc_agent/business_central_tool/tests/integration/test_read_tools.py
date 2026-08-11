import asyncio

from business_central_tool.app.integrations.business_central.tools.company_tools import (
    get_companies,
    validate_company,
)
from business_central_tool.app.integrations.business_central.tools.customer_tools import (
    list_customers,
    get_customer,
)


class FakeCompanyService:
    async def get_companies(self):
        return [
            {
                "id": "company-1",
                "name": "CRONUS IN",
            },
            {
                "id": "company-2",
                "name": "My Company",
            },
        ]

    async def validate_company(self, company_id: str):
        return {
            "id": company_id,
            "name": "CRONUS IN",
        }


class FakeCustomerService:
    async def list_customers(
        self,
        company_id: str,
        *,
        top: int = 100,
        skip: int = 0,
    ):
        return [
            {
                "id": "customer-1",
                "number": "10000",
                "displayName": "Adatum Corporation",
            },
            {
                "id": "customer-2",
                "number": "20000",
                "displayName": "Trey Research",
            },
        ]

    async def get_customer(
        self,
        company_id: str,
        customer_id: str,
    ):
        return {
            "id": customer_id,
            "number": "10000",
            "displayName": "Adatum Corporation",
        }


async def main():

    company_service = FakeCompanyService()
    customer_service = FakeCustomerService()

    # ---------------------------------------------------------
    # Test 1: Get Companies
    # ---------------------------------------------------------


    companies = await get_companies(
        company_service
    )


    for company in companies:
        print(
            f"ID: {company['id']} | "
            f"Name: {company['name']}"
        )

    # ---------------------------------------------------------
    # Test 2: Validate Company
    # ---------------------------------------------------------


    company = await validate_company(
        company_service,
        "company-1",
    )

    print(
        f"Validated company: "
        f"{company['name']}"
    )

    # ---------------------------------------------------------
    # Test 3: List Customers
    # ---------------------------------------------------------


    customers = await list_customers(
        customer_service,
        "company-1",
        top=10,
        skip=0,
    )

    print(
        f"Customers returned: "
        f"{len(customers)}"
    )

    for customer in customers:
        print(
            f"Number: {customer['number']} | "
            f"Name: {customer['displayName']}"
        )

    # ---------------------------------------------------------
    # Test 4: Get Customer
    # ---------------------------------------------------------


    customer = await get_customer(
        customer_service,
        "company-1",
        "customer-1",
    )

    print(
        f"Customer returned: "
        f"{customer['displayName']}"
    )


if __name__ == "__main__":
    asyncio.run(main())