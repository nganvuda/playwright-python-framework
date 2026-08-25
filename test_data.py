from dataclasses import dataclass
from utils.config import TEST_EMAIL, TEST_PASSWORD

@dataclass
class User:
    email: str
    password: str

INVALID_USER = User(email="wrongemail@example.com", password="wrongpassword")
VALID_USER = User(email= TEST_EMAIL, password= TEST_PASSWORD)
PRODUCT_NAME = "Pliers"
