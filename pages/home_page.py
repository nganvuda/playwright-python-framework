from playwright.sync_api import Page, Locator, expect
from components.header_component import HeaderComponent
from pages.login_page import LoginPage
from utils.config import BASE_URL
from pages.base_page import BasePage
import re
from pages.product_page import ProductPage
import logging
logger = logging.getLogger(__name__)


class HomePage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.search_input: Locator = page.locator('[data-test="search-query"]')
        self.search_button: Locator = page.locator('[data-test="search-submit"]')

    def open(self) -> None:
        logger.info(f"Opening Home Page: {BASE_URL}")
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("domcontentloaded")

    def go_to_login(self) -> LoginPage:
        logger.info("Going to Login Page")
        self.header.click_sign_in()
        return LoginPage(self.page)

    def select_product(self, name: str) -> ProductPage:
        logger.info(f"Selecting product {name}")
        card = self.page.locator(f'[data-test="product-name"]:text-is("{name}")')
        card.click()
        return ProductPage(self.page)

    def search_product(self, term: str) -> None:
        logger.info(f"Searching product {term}")
        self.search_input.fill(term)
        self.search_button.click()
        expect(self.page.get_by_text(f"Searched for: {term}")).to_be_visible()