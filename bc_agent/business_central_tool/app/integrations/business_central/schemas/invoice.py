from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class InvoiceResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: UUID
    number: str

    external_document_number: str | None = None

    invoice_date: date | None = None
    posting_date: date | None = None
    due_date: date | None = None

    customer_id: UUID | None = None
    customer_number: str | None = None
    customer_name: str | None = None

    currency_code: str | None = None

    total_amount_excluding_tax: Decimal | None = None
    total_tax_amount: Decimal | None = None
    total_amount_including_tax: Decimal | None = None

    status: str | None = None

    last_modified_date_time: datetime | None = None