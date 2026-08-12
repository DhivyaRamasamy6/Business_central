from business_central_tool.app.integrations.business_central.client.business_central_client import (
    BusinessCentralClient,
)
from business_central_tool.app.integrations.business_central.client.endpoints import (
    BusinessCentralEndpoints,
)
from business_central_tool.app.integrations.business_central.schemas.invoice import (
    InvoiceResponse,
)

from .base_service import BaseBusinessCentralService


class InvoiceService(BaseBusinessCentralService):
    """
    Business Central Sales Invoice domain service.

    This layer handles invoice business operations and does not
    contain authentication or HTTP implementation details.
    """

    async def list_invoices(
        self,
        company_id: str,
        *,
        top: int = 100,
        skip: int = 0,
    ) -> list[InvoiceResponse]:

        if top < 1 or top > 1000:
            raise ValueError(
                "top must be between 1 and 1000."
            )

        if skip < 0:
            raise ValueError(
                "skip cannot be negative."
            )

        response = await self.client.get(
            BusinessCentralEndpoints.invoices(
                company_id
            ),
            params={
                "$top": top,
                "$skip": skip,
            },
        )

        return [
            InvoiceResponse.model_validate(invoice)
            for invoice in response.get("value", [])
        ]

    async def get_invoice(
        self,
        company_id: str,
        invoice_id: str,
    ) -> InvoiceResponse:

        response = await self.client.get(
            BusinessCentralEndpoints.invoice(
                company_id,
                invoice_id,
            )
        )

        return InvoiceResponse.model_validate(response)