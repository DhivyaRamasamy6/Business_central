from fastapi import APIRouter, Depends, Query

from business_central_tool.app.integrations.business_central.schemas.customer import (
    CustomerResponse,
)
from business_central_tool.app.integrations.business_central.services.customer_service import (
    CustomerService,
)

from .dependencies import get_customer_service


router = APIRouter(
    prefix="/api/business-central",
    tags=["Business Central - Customers"],
)


@router.get(
    "/companies/{company_id}/customers",
    response_model=list[CustomerResponse],
    summary="List Business Central customers",
    description="Retrieve customers for a Business Central company.",
)
async def list_customers(
    company_id: str,
    top: int = Query(
        default=100,
        ge=1,
        le=1000,
        description="Maximum number of customers to return.",
    ),
    skip: int = Query(
        default=0,
        ge=0,
        description="Number of customers to skip.",
    ),
    customer_service: CustomerService = Depends(get_customer_service),
) -> list[CustomerResponse]:
    """
    Retrieve customers from a Business Central company.
    """
    return await customer_service.list_customers(
        company_id=company_id,
        top=top,
        skip=skip,
    )


@router.get(
    "/companies/{company_id}/customers/{customer_id}",
    response_model=CustomerResponse,
    summary="Get Business Central customer",
    description="Retrieve a single Business Central customer by ID.",
)
async def get_customer(
    company_id: str,
    customer_id: str,
    customer_service: CustomerService = Depends(get_customer_service),
) -> CustomerResponse:
    """
    Retrieve a single customer from Business Central.
    """
    return await customer_service.get_customer(
        company_id=company_id,
        customer_id=customer_id,
    )