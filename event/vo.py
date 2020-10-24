from pydantic import validator
from pydantic.main import BaseModel

from base.extension import ExtendedEnum


class Currency(str, ExtendedEnum):
    KRW = "KRW"
    USD = "USD"


class Money(BaseModel):
    amount: int
    currency: Currency

    @validator('amount')
    def amount_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("amount should be greater than 0")
        return v
