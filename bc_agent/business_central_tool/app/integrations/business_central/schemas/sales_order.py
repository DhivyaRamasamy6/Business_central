from datetime import date, datetime
from uuid import UUID

from pydantic import AliasChoices, BaseModel, ConfigDict, Field


class SalesOrderResponse(BaseModel):
    """
    Business Central Sales Order response model.

    Maps Business Central camelCase JSON fields to
    Python snake_case fields.
    """

    model_config = ConfigDict(
        extra="ignore",
        populate_by_name=True,
    )

    id: UUID

    number: str

    external_document_number: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "externalDocumentNumber",
            "external_document_number",
        ),
    )

    order_date: date | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orderDate",
            "order_date",
        ),
    )

    posting_date: date | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "postingDate",
            "posting_date",
        ),
    )

    customer_id: UUID | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "customerId",
            "customer_id",
        ),
    )

    customer_number: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "customerNumber",
            "customer_number",
        ),
    )

    customer_name: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "customerName",
            "customer_name",
        ),
    )

    bill_to_name: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "billToName",
            "bill_to_name",
        ),
    )

    ship_to_name: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "shipToName",
            "ship_to_name",
        ),
    )

    ship_to_contact: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "shipToContact",
            "ship_to_contact",
        ),
    )

    currency_code: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "currencyCode",
            "currency_code",
        ),
    )

    payment_terms_id: UUID | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "paymentTermsId",
            "payment_terms_id",
        ),
    )

    shipment_method_id: UUID | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "shipmentMethodId",
            "shipment_method_id",
        ),
    )

    salesperson: str | None = None

    last_modified_date_time: datetime | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "lastModifiedDateTime",
            "last_modified_date_time",
        ),
    )