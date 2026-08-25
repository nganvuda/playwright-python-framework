from playwright.sync_api import Locator, Page, expect
import logging
logger = logging.getLogger(__name__)

class HeaderComponent:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.sign_in_link: Locator = page.get_by_role(
            "link",
            name="Sign In",
        )
        self.account_menu: Locator = page.locator('[data-test="nav-menu"]')
        self.cart_count: Locator = page.locator('[data-test="cart-quantity"]')

    def click_sign_in(self) -> None:
        logger.info("Clicking Sign In link")
        self.sign_in_link.click()
    def should_show_logged_in_user(self) -> None:
        logger.info("User logged in")
        expect(self.account_menu).to_be_visible()
    def should_show_cart_count(self, count: str) -> None:
        logger.info(f"Asserting card count is {count}")
        expect(self.cart_count).to_have_text(count)
