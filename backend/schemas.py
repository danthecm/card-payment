from pydantic import BaseModel

class PaymentSchema(BaseModel):
    """
    Payment Schema Model
    """
    name: str
    card_number: int 
    expiry_date: str
    cvv: int 

