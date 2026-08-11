from uuid import UUID

from business_central_tool.app.core.exceptions import InvalidCompanyError

from ..client.business_central_client import BusinessCentralClient
from ..client.endpoints import BusinessCentralEndpoints


class CompanyService:

    def __init__(
        self,
        client: BusinessCentralClient,
    ) -> None:
        self.client = client

    async def get_companies(self) -> list[dict]:

        response = await self.client.get(
            BusinessCentralEndpoints.companies()
        )

        return response.get("value", [])

    async def validate_company(
        self,
        company_id: str,
    ) -> dict:

        try:
            UUID(company_id)
        except ValueError as exc:
            raise InvalidCompanyError(
                f"Invalid company ID: {company_id}"
            ) from exc

        companies = await self.get_companies()

        for company in companies:
            if company.get("id") == company_id:
                return company

        raise InvalidCompanyError(
            f"Company does not exist: {company_id}"
        )