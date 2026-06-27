import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_KEY_TIMEOUT = os.getenv("JET_KWY_TIMEOUT")


    