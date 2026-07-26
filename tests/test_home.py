from playwright.sync_api import Page, expect
from pages.home_page import HomePage


def test_home_page_loads(page: Page) -> None:
    home = HomePage(page)
    home.open()

    expect(home.page_heading).to_be_visible()