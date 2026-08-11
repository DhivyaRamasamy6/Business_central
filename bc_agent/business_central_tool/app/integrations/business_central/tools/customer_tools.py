from ..schemas.customer import CustomerResponse
from ..services.customer_service import CustomerService


async def list_customers(
    customer_service: CustomerService,
    company_id: str,
    *,
    top: int = 100,
    skip: int = 0,
) -> list[CustomerResponse]:
    """
    Retrieve customers from a Business Central company.
    """

    return await customer_service.list_customers(
        company_id,
        top=top,
        skip=skip,
    )

async def get_customer(
    customer_service: CustomerService,
    company_id: str,
    customer_id: str,
) -> CustomerResponse:
    """
    Retrieve a single customer from Business Central.
    """

    return await customer_service.get_customer(
        company_id,
        customer_id,
    )