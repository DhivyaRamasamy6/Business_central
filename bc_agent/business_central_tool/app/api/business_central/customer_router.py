from fastapi import APIRouter, Depends, Query, status

from business_central_tool.app.integrations.business_central.schemas.customer import (
    CustomerCreateRequest,
    CustomerResponse,
    CustomerUpdateRequest,
)

from business_central_tool.app.integrations.business_central.services.customer_service import (
    CustomerService,
)

from .dependencies import get_customer_service


router = APIRouter(
    prefix="/api/business-central",
    tags=["Business Central - Customers"],
)


# ============================================================
# GET CUSTOMERS
# ============================================================

@router.get(
    "/companies/{company_id}/customers",
    response_model=list[CustomerResponse],
    summary="List Business Central customers",
    description=(
        "Retrieve customers for a Business Central company."
    ),
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
    customer_service: CustomerService = Depends(
        get_customer_service
    ),
) -> list[CustomerResponse]:

    return await customer_service.list_customers(
        company_id=company_id,
        top=top,
        skip=skip,
    )


# ============================================================
# GET CUSTOMER BY ID
# ============================================================

@router.get(
    "/companies/{company_id}/customers/{customer_id}",
    response_model=CustomerResponse,
    summary="Get Business Central customer",
    description=(
        "Retrieve a single Business Central customer by ID."
    ),
)
async def get_customer(
    company_id: str,
    customer_id: str,
    customer_service: CustomerService = Depends(
        get_customer_service
    ),
) -> CustomerResponse:

    return await customer_service.get_customer(
        company_id=company_id,
        customer_id=customer_id,
    )


# ============================================================
# CREATE CUSTOMER
# ============================================================

@router.post(
    "/companies/{company_id}/customers",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Business Central customer",
    description=(
        "Create a new customer in a Business Central company."
    ),
)
async def create_customer(
    company_id: str,
    request: CustomerCreateRequest,
    customer_service: CustomerService = Depends(
        get_customer_service
    ),
) -> CustomerResponse:

    return await customer_service.create_customer(
        company_id=company_id,
        request=request,
    )


# ============================================================
# UPDATE CUSTOMER
# ============================================================

@router.patch(
    "/companies/{company_id}/customers/{customer_id}",
    response_model=CustomerResponse,
    summary="Update Business Central customer",
    description=(
        "Update an existing Business Central customer. "
        "The current ETag must be provided for concurrency control."
    ),
)
async def update_customer(
    company_id: str,
    customer_id: str,
    request: CustomerUpdateRequest,
    etag: str = Query(
        ...,
        description=(
            "Current Business Central ETag of the customer."
        ),
    ),
    customer_service: CustomerService = Depends(
        get_customer_service
    ),
) -> CustomerResponse:

    return await customer_service.update_customer(
        company_id=company_id,
        customer_id=customer_id,
        request=request,
        etag=etag,
    )


# ============================================================
# DELETE CUSTOMER
# ============================================================

@router.delete(
    "/companies/{company_id}/customers/{customer_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Business Central customer",
    description=(
        "Delete an existing Business Central customer. "
        "The current ETag must be provided for concurrency control."
    ),
)
async def delete_customer(
    company_id: str,
    customer_id: str,
    etag: str = Query(
        ...,
        description=(
            "Current Business Central ETag of the customer."
        ),
    ),
    customer_service: CustomerService = Depends(
        get_customer_service
    ),
) -> None:

    await customer_service.delete_customer(
        company_id=company_id,
        customer_id=customer_id,
        etag=etag,
    )