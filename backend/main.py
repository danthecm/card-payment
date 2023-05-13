from fastapi import FastAPI, Request

app = FastAPI()


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
