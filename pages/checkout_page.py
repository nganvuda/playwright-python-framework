from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage
from components.login_form_component import LoginFormComponent
import logging

from test_data import Address

logger = logging.getLogger(__name__)


class CheckoutPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.proceed_from_cart_button: Locator = page.locator('[data-test="proceed-1"]')
        self.proceed_from_signin_button: Locator = page.locator('[data-test="proceed-2"]')
        self.form = LoginFormComponent(page)
        self.country_input: Locator = page.locator('[data-test="country"]')
        self.postal_code_input: Locator = page.locator('[data-test="postal_code"]')
        self.house_number_input: Locator = page.locator('[data-test="house_number"]')
        self.street_input: Locator = page.locator('[data-test="street"]')
        self.city_input: Locator = page.locator('[data-test="city"]')
        self.state_input: Locator = page.locator('[data-test="state"]')
        self.proceed_from_address_button: Locator = page.locator('[data-test="proceed-3"]')

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

    def fill_billing_address(self, address: "Address") -> None:
        logger.info(f"Filling billing address: {address}")
        self.country_input.select_option(address.country)
        self.postal_code_input.fill(address.postal_code)
        self.house_number_input.fill(address.house_number)
        self.street_input.fill(address.street)
        self.city_input.fill(address.city)
        self.state_input.fill(address.state)

    def proceed_from_address(self) -> None:
        logger.info("Proceeding from billing address to payment step")
        self.proceed_from_address_button.click()