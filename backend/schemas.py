from pydantic import BaseModel, validator
from datetime import date
from helpers import validate_length


class PaymentSchema(BaseModel):
    """
    Payment Schema Model
    """
    name: str
    card_number: str
    expiry_date: str
    cvv: int

    @validator('card_number')
    def validate_card_number(cls, value):
        is_valid = validate_length(value, 16, 19)
        if not is_valid:
            raise ValueError("Invalid! Card number must be 16-19 digits")
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
                    "Invalid! Your card has expired")
        return value

    @validator('cvv')
    def validate_cvv(cls, value: int, values) -> int:
        card_number = values.get('card_number')
        if not card_number:
            return value
        card_start_value = str(card_number)[:2]
        min_len = 3
        max_len = 3
        if card_start_value in ["34", "37"]:
            min_len = 4
            max_len = 4
        is_valid = validate_length(value, min_len, max_len)
        if not is_valid:
            raise ValueError(
                "Invalid cvv for card type")
        return value
