from fastapi import APIRouter, Depends, Query

from business_central_tool.app.integrations.business_central.schemas.invoice import (
    InvoiceResponse,
)
from business_central_tool.app.integrations.business_central.services.invoice_service import (
    InvoiceService,
)

from .dependencies import get_invoice_service


router = APIRouter(
    prefix="/api/business-central",
    tags=["Business Central - Invoices"],
)


@router.get(
    "/companies/{company_id}/invoices",
    response_model=list[InvoiceResponse],
    summary="List Business Central sales invoices",
)
async def list_invoices(
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
    invoice_service: InvoiceService = Depends(
        get_invoice_service
    ),
) -> list[InvoiceResponse]:

    return await invoice_service.list_invoices(
        company_id=company_id,
        top=top,
        skip=skip,
    )


@router.get(
    "/companies/{company_id}/invoices/{invoice_id}",
    response_model=InvoiceResponse,
    summary="Get Business Central sales invoice",
)
async def get_invoice(
    company_id: str,
    invoice_id: str,
    invoice_service: InvoiceService = Depends(
        get_invoice_service
    ),
) -> InvoiceResponse:

    return await invoice_service.get_invoice(
        company_id=company_id,
        invoice_id=invoice_id,
    )