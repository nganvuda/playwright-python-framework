from playwright.sync_api import Page, expect
from pages.home_page import HomePage


def test_home_page_loads(home_page) -> None:
    home_page.open()

    expect(home_page.page).to_have_url("https://practicesoftwaretesting.com/")