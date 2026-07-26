import os

ENV = os.getenv("ENV", "qa")

URL = {
    "qa" : "https://practicesoftwaretesting.com",
    "staging" : "https://staging.practicesoftwaretesting.com",
    "production" : "https://prod.practicesoftwaretesting.com",
}

BASE_URL = URL.get(ENV, URL["qa"])