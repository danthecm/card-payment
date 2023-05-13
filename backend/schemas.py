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

 