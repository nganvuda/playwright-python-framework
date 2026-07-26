import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.fixture
def home_page(page):
    return HomePage(page)
@pytest.fixture
def login_page(page):
    return LoginPage(page)
