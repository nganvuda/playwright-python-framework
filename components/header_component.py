from playwright.sync_api import Locator, Page
from pages.login_page import LoginPage

class HeaderComponent:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.sign_in_link: Locator = page.get_by_role(
            "link",
            name="Sign In",
        )

    def click_sign_in(self) -> None:
        self.sign_in_link.click()


