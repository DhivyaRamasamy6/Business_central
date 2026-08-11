from uuid import UUID

from business_central_tool.app.core.exceptions import InvalidCompanyError

from ..client.business_central_client import BusinessCentralClient
from ..client.endpoints import BusinessCentralEndpoints
from ..schemas.customer import (
    CustomerCreateRequest,
    CustomerResponse,
    CustomerUpdateRequest,
)
from .base_service import BaseBusinessCentralService


class CustomerService(BaseBusinessCentralService):
    """
    Business Central Customer domain service.

    This layer knows business operations but does not know
    authentication or HTTP implementation details.
    """

    async def list_customers(
        self,
        company_id: str,
        *,
        top: int = 100,
        skip: int = 0,
    ) -> list[CustomerResponse]:

        if top < 1 or top > 1000:
            raise ValueError(
                "top must be between 1 and 1000."
            )

        if skip < 0:
            raise ValueError(
                "skip cannot be negative."
            )

        response = await self.client.get(
            BusinessCentralEndpoints.customers(
                company_id
            ),
            params={
                "$top": top,
                "$skip": skip,
            },
        )

        return [
            CustomerResponse.model_validate(customer)
            for customer in response.get("value", [])
        ]

    async def get_customer(
        self,
        company_id: str,
        customer_id: str,
    ) -> CustomerResponse:

        response = await self.client.get(
            BusinessCentralEndpoints.customer(
                company_id,
                customer_id,
            )
        )

        return CustomerResponse.model_validate(response)

    async def create_customer(
        self,
        company_id: str,
        request: CustomerCreateRequest,
    ) -> CustomerResponse:

        response = await self.client.post(
            BusinessCentralEndpoints.customers(
                company_id
            ),
            payload=request.model_dump(
                exclude_none=True
            ),
        )

        return CustomerResponse.model_validate(response)

    async def update_customer(
        self,
        company_id: str,
        customer_id: str,
        request: CustomerUpdateRequest,
        *,
        etag: str | None = None,
    ) -> CustomerResponse:

        response = await self.client.patch(
            BusinessCentralEndpoints.customer(
                company_id,
                customer_id,
            ),
            payload=request.model_dump(
                exclude_none=True
            ),
            etag=etag,
        )

        return CustomerResponse.model_validate(response)

    async def delete_customer(
        self,
        company_id: str,
        customer_id: str,
        *,
        etag: str | None = None,
    ) -> None:

        await self.client.delete(
            BusinessCentralEndpoints.customer(
                company_id,
                customer_id,
            ),
            etag=etag,
        )