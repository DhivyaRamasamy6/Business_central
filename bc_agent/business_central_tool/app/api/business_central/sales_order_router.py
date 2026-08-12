from fastapi import APIRouter, Depends, Query

from business_central_tool.app.integrations.business_central.schemas.sales_order import (
    SalesOrderResponse,
)
from business_central_tool.app.integrations.business_central.services.sales_order_service import (
    SalesOrderService,
)

from .dependencies import get_sales_order_service


router = APIRouter(
    prefix="/api/business-central",
    tags=["Business Central - Sales Orders"],
)


@router.get(
    "/companies/{company_id}/sales-orders",
    response_model=list[SalesOrderResponse],
    summary="List Business Central sales orders",
)
async def list_sales_orders(
    company_id: str,
    top: int = Query(
        default=100,
        ge=1,
        le=1000,
    ),
    skip: int = Query(
        default=0,
        ge=0,
    ),
    sales_order_service: SalesOrderService = Depends(
        get_sales_order_service
    ),
) -> list[SalesOrderResponse]:

    return await sales_order_service.list_sales_orders(
        company_id=company_id,
        top=top,
        skip=skip,
    )


@router.get(
    "/companies/{company_id}/sales-orders/{sales_order_id}",
    response_model=SalesOrderResponse,
    summary="Get Business Central sales order",
)
async def get_sales_order(
    company_id: str,
    sales_order_id: str,
    sales_order_service: SalesOrderService = Depends(
        get_sales_order_service
    ),
) -> SalesOrderResponse:

    return await sales_order_service.get_sales_order(
        company_id=company_id,
        sales_order_id=sales_order_id,
    )