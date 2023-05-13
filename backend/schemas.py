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
            raise ValueError("Invalid card number length. Card number must be 16-19 characters")
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

    @validator('cvv')
    def validate_cvv(cls, value: int, values) -> int:
        card_number = values.get('card_number')
        card_start_value = str(card_number)[:2]
        min_len = 3
        max_len = 3
        if card_start_value in ["34", "37"]:
            min_len = 4
            max_len = 4
        is_valid = validate_length(value, min_len, max_len)
        if not is_valid:
            raise ValueError(
                "Invalid CVV. CVV length should be equal to 3 or 4 for american express cards")
        return value
