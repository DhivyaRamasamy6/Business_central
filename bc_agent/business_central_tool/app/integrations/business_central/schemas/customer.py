from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator


class CustomerType(str, Enum):
    COMPANY = "Company"
    PERSON = "Person"


class CustomerBlocked(str, Enum):
    NONE = " "
    SHIP = "Ship"
    INVOICE = "Invoice"
    ALL = "All"


class CustomerResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: UUID
    number: str
    displayName: str
    type: CustomerType | None = None

    addressLine1: str | None = None
    addressLine2: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    postalCode: str | None = None

    phoneNumber: str | None = None
    email: str | None = None
    website: str | None = None

    taxLiable: bool | None = None
    taxRegistrationNumber: str | None = None

    currencyCode: str | None = None
    paymentTermsId: UUID | None = None
    shipmentMethodId: UUID | None = None
    paymentMethodId: UUID | None = None

    blocked: CustomerBlocked | None = None

    lastModifiedDateTime: datetime | None = None

    @field_validator("blocked", mode="before")
    @classmethod
    def normalize_blocked(cls, value):
        print(f"DEBUG VALIDATOR INPUT: {value!r}")

        if value is None:
            return None

        if isinstance(value, str):
            normalized = value.strip()

            if normalized in {
                "_x0020_",
                "*x0020*",
                r"\u0020",
                "",
            }:
                print("DEBUG: Converting encoded blank to SPACE")
                return CustomerBlocked.NONE.value

        return value

class CustomerCreateRequest(BaseModel):
    displayName: str = Field(min_length=1, max_length=100)
    type: CustomerType = CustomerType.COMPANY

    addressLine1: str | None = None
    addressLine2: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    postalCode: str | None = None

    phoneNumber: str | None = None
    email: str | None = None
    website: str | None = None


class CustomerUpdateRequest(BaseModel):
    displayName: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    addressLine1: str | None = None
    addressLine2: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    postalCode: str | None = None

    phoneNumber: str | None = None
    email: str | None = None
    website: str | None = None