from dataclasses import dataclass
from utils.config import TEST_EMAIL, TEST_PASSWORD

@dataclass
class User:
    email: str
    password: str

@dataclass
class Address:
    street: str
    city: str
    state: str
    postal_code: str
    house_number: str
    country: str

INVALID_USER = User(email="wrongemail@example.com", password="wrongpassword")
VALID_USER = User(email= TEST_EMAIL, password= TEST_PASSWORD)
PRODUCT_NAME = "Pliers"
TEST_ADDRESS = Address(
    country="Australia",
    postal_code="12345",
    house_number="123",
    street="Main Street",
    city="Anytown",
    state="California",
)