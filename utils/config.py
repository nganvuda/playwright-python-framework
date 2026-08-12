import os
from dotenv import load_dotenv

load_dotenv()
ENV = os.getenv("ENV", "qa")

URL = {
    "qa" : "https://practicesoftwaretesting.com/",
    "staging" : "https://staging.practicesoftwaretesting.com",
    "production" : "https://prod.practicesoftwaretesting.com",
}

BASE_URL = URL.get(ENV, URL["qa"])

TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")

if not TEST_EMAIL or not TEST_PASSWORD:
    raise ValueError(
        "TEST_EMAIL / TEST_PASSWORD not set. Copy .env.example to .env and fill in real values."
    )
