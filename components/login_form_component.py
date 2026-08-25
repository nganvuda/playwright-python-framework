from playwright.sync_api import Page, Locator, expect
import logging
logger = logging.getLogger(__name__)


class LoginFormComponent:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.email_input: Locator = page.locator('[data-test="email"]')
        self.password_input: Locator = page.locator('[data-test="password"]')
        self.login_button: Locator = page.get_by_role("button", name="login")
        self.login_error: Locator = page.get_by_text(
            "Invalid email or password", exact=True
        )

    def login(self, email: str, password: str) -> None:
        logger.info("Submitting login form")
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def should_show_invalid_credentials_error(self) -> None:
        logger.info("Asserting invalid credentials error is visible")
        expect(self.login_error).to_be_visible()