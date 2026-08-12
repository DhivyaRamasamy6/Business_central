from typing import Any

from fastapi import APIRouter, Depends

from business_central_tool.app.integrations.business_central.services.company_service import (
    CompanyService,
)

from .dependencies import get_company_service


router = APIRouter(
    prefix="/api/business-central",
    tags=["Business Central - Companies"],
)


@router.get(
    "/companies",
    response_model=list[dict[str, Any]],
    summary="List Business Central companies",
    description="Retrieve all companies available to the authenticated Business Central account.",
)
async def list_companies(
    company_service: CompanyService = Depends(get_company_service),
) -> list[dict[str, Any]]:
    """
    Retrieve all Business Central companies.
    """
    return await company_service.get_companies()


@router.get(
    "/companies/{company_id}",
    response_model=dict[str, Any],
    summary="Get Business Central company",
    description="Validate and retrieve a Business Central company by ID.",
)
async def get_company(
    company_id: str,
    company_service: CompanyService = Depends(get_company_service),
) -> dict[str, Any]:
    """
    Retrieve a Business Central company by ID.
    """
    return await company_service.validate_company(company_id)