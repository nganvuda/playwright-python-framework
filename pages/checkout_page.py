from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage
from components.login_form_component import LoginFormComponent
import logging
logger = logging.getLogger(__name__)


class CheckoutPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.proceed_from_cart_button: Locator = page.locator('[data-test="proceed-1"]')
        self.proceed_from_signin_button: Locator = page.locator('[data-test="proceed-2"]')
        self.form = LoginFormComponent(page)

    def proceed_from_cart(self) -> None:
        logger.info("Proceeding from cart to sign in step")
        self.proceed_from_cart_button.click()

    def proceed_from_signin(self) -> None:
        logger.info("Proceeding from signin to billing address step")
        expect(self.page.get_by_text("you are already logged in")).to_be_visible()
        self.proceed_from_signin_button.click()

    def should_be_on_billing_address_step(self) -> None:
        logger.info("Asserting billing address step is active")
        expect(self.page.get_by_role("heading", name="Billing Address")).to_be_visible()