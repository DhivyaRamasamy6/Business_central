import asyncio

from business_central_tool.app.core.config import settings
from business_central_tool.app.integrations.business_central import (
    create_business_central_services,
)


async def main() -> None:
    print("Starting Business Central integration test...")

    services = create_business_central_services()

    # ---------------------------------------------
    # 1. Test authentication + companies endpoint
    # ---------------------------------------------

    print("\nFetching companies...")

    companies = await services["companies"].get_companies()

    print(f"Companies found: {len(companies)}")

    for company in companies:
        print(
            f"ID: {company['id']}"
            f" | Name: {company['name']}"
        )

    # ---------------------------------------------
    # 2. Test customer endpoint
    # ---------------------------------------------

    print("\nFetching customers...")

    customers = await services["customers"].list_customers(
        settings.bc_company_id,
        top=10,
    )

    print(f"Customers found: {len(customers)}")

    for customer in customers:
        print(
            f"Number: {customer.number}"
            f" | Name: {customer.displayName}"
        )

    print("\nBusiness Central integration test completed.")


if __name__ == "__main__":
    asyncio.run(main())