from fastapi.middleware.cors import CORSMiddleware
from main import app

allowed_origins = ["*"]
allowed_headers = ["*"]
allowed_methods = ["GET", "POST"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods= allowed_methods,
    allow_headers=allowed_headers,
)