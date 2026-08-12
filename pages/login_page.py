from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage
import logging
logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input: Locator = page.get_by_label("Email")
        self.password_input: Locator = page.locator('[data-test="password"]')
        self.login_button: Locator = page.get_by_role("button", name= "Login")
        self.login_error: Locator = page.get_by_text(
            "Invalid email or password", exact=True)

    def login(self, email : str, password : str) -> None:
        logger.info("Submitting login form")
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def should_show_invalid_credentials_error(self) -> None:
        logger.info("Asserting invalid credentials error is visible")
        expect(self.login_error).to_be_visible()