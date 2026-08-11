from uuid import UUID

from business_central_tool.app.core.config import settings
from business_central_tool.app.core.exceptions import InvalidCompanyError


class BusinessCentralEndpoints:
    """
    Centralized Business Central API endpoint construction.

    The LLM never constructs these URLs.
    """

    @staticmethod
    def _validate_uuid(value: str, field_name: str) -> str:
        try:
            UUID(value)
        except ValueError as exc:
            raise InvalidCompanyError(
                f"Invalid {field_name}: {value}"
            ) from exc

        return value

    @classmethod
    def base_url(cls) -> str:
        return (
            f"{settings.bc_base_url.rstrip('/')}"
            f"/v2.0"
            f"/{settings.bc_tenant_id}"
            f"/{settings.bc_environment}"
            f"/api"
            f"/{settings.bc_api_version}"
        )

    @classmethod
    def companies(cls) -> str:
        return f"{cls.base_url()}/companies"

    @classmethod
    def company(cls, company_id: str) -> str:
        company_id = cls._validate_uuid(
            company_id,
            "company_id",
        )

        return f"{cls.companies()}({company_id})"

    @classmethod
    def customers(cls, company_id: str) -> str:
        return f"{cls.company(company_id)}/customers"

    @classmethod
    def customer(
        cls,
        company_id: str,
        customer_id: str,
    ) -> str:
        customer_id = cls._validate_uuid(
            customer_id,
            "customer_id",
        )

        return f"{cls.customers(company_id)}({customer_id})"