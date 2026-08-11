import asyncio

from business_central_tool.app.core.config import settings
from business_central_tool.app.integrations.business_central import (
    create_business_central_services,
)


async def main() -> None:

    services = create_business_central_services()

    # ---------------------------------------------
    # 1. Test authentication + companies endpoint
    # ---------------------------------------------

    companies = await services["companies"].get_companies()

    for company in companies:
        print(
            f"ID: {company['id']}"
            f" | Name: {company['name']}"
        )

    # ---------------------------------------------
    # 2. Test customer endpoint
    # ---------------------------------------------


    customers = await services["customers"].list_customers(
        settings.bc_company_id,
        top=10,
    )


    for customer in customers:
        print(
            f"Number: {customer.number}"
            f" | Name: {customer.displayName}"
        )

    print("\nBusiness Central integration test completed.")


if __name__ == "__main__":
    asyncio.run(main())