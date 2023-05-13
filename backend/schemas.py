from pydantic import BaseModel, validator
from datetime import date
from helpers import validate_length


class PaymentSchema(BaseModel):
    """
    Payment Schema Model
    """
    name: str
    card_number: int
    expiry_date: str
    cvv: int

    @validator('card_number')
    def validate_card_number(cls, value):
        is_valid = validate_length(value, 16, 19)
        if not is_valid:
            raise ValueError("Invalid card number length")
        return value

    @validator('expiry_date')
    def validate_expirty_date(cls, value: str) -> str:
        try:
            date_parts = value.split('/')
            month = int(date_parts[0])
            year = int(date_parts[1])
            input_date = date(year=year, month=month, day=1)
        except (IndexError, ValueError):
            raise ValueError(
                "Invalid date format. Please use MM/YYYY e.g 05/2023.")
        else:
            if input_date < date.today().replace(day=1):
                raise ValueError(
                    "Invalid date. Date should be greater than or equal to the current month.")
        return value
