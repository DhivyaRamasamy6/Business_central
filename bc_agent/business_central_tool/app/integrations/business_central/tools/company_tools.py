from typing import Any

from ..services.company_service import CompanyService


async def get_companies(
    company_service: CompanyService,
) -> list[dict[str, Any]]:
    """
    Retrieve all companies available in Business Central.
    """

    return await company_service.get_companies()


async def validate_company(
    company_service: CompanyService,
    company_id: str,
) -> dict[str, Any]:
    """
    Validate that a Business Central company exists.
    """

    return await company_service.validate_company(company_id)