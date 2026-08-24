from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
import logging
logger = logging.getLogger(__name__)

class ProductPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.add_to_cart_button: Locator = page.locator('[data-test="add-to-cart"]')

    def add_to_cart(self) -> None:
        logger.info("Click on the add to-cart button")
        self.add_to_cart_button.click()