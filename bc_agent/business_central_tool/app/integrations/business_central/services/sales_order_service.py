from business_central_tool.app.integrations.business_central.client.business_central_client import (
    BusinessCentralClient,
)
from business_central_tool.app.integrations.business_central.client.endpoints import (
    BusinessCentralEndpoints,
)
from business_central_tool.app.integrations.business_central.schemas.sales_order import (
    SalesOrderResponse,
)

from .base_service import BaseBusinessCentralService


class SalesOrderService(BaseBusinessCentralService):
    """
    Business Central Sales Order domain service.

    This layer handles sales order business operations
    and does not contain authentication or HTTP
    implementation details.
    """

    async def list_sales_orders(
        self,
        company_id: str,
        *,
        top: int = 100,
        skip: int = 0,
    ) -> list[SalesOrderResponse]:
        """
        Retrieve sales orders for a Business Central company.
        """

        if top < 1 or top > 1000:
            raise ValueError(
                "top must be between 1 and 1000."
            )

        if skip < 0:
            raise ValueError(
                "skip cannot be negative."
            )

        response = await self.client.get(
            BusinessCentralEndpoints.sales_orders(
                company_id
            ),
            params={
                "$top": top,
                "$skip": skip,
            },
        )

        return [
            SalesOrderResponse.model_validate(
                sales_order
            )
            for sales_order in response.get(
                "value",
                [],
            )
        ]

    async def get_sales_order(
        self,
        company_id: str,
        sales_order_id: str,
    ) -> SalesOrderResponse:
        """
        Retrieve a single Business Central sales order.
        """

        response = await self.client.get(
            BusinessCentralEndpoints.sales_order(
                company_id,
                sales_order_id,
            )
        )

        return SalesOrderResponse.model_validate(
            response
        )