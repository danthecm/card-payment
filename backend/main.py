from fastapi import Request
from schemas import PaymentSchema
from config import app

@app.get('/')
async def index(request: Request):
    """
    Returns basic information about the API 
    """
    base_url = request.base_url
    return {
        "message": "Evaluation API",
        "version": "0.1",
        "docs": [f"{base_url}docs", f"{base_url}redoc"]
    }


@app.post("/payment")
async def payment(data: PaymentSchema):
    """
    Process a payment request

    Returns:
    dict: message: success -> if successful
    dict: detail: list of error information -> if an error occurs
    """
    return {"message": "success"}
