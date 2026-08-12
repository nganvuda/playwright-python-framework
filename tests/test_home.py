import pytest
from playwright.sync_api import Page, expect
from utils.config import BASE_URL
from pages.home_page import HomePage

@pytest.mark.smoke
def test_home_page_loads(home_page) -> None:
    home_page.open()
    expect(home_page.page).to_have_url(BASE_URL)