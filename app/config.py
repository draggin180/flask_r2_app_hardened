import os

class Config:
    SECRET_API_KEY = os.getenv("SECRET_API_KEY")
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "").split(",")
    RATE_LIMIT = os.getenv("RATE_LIMIT", "10/minute")
