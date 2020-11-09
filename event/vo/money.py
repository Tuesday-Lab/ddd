from pydantic import validator
from pydantic.main import BaseModel

from event.vo.currency import Currency


class Money(BaseModel):
    amount: int
    currency: Currency

    @validator('amount')
    def amount_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("amount should be grater than 0")
        return v
