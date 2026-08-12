import pytest
from utils.logger import setup_logging
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.fixture
def home_page(page):
    return HomePage(page)
@pytest.fixture
def login_page(page):
    return LoginPage(page)
@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    setup_logging()
