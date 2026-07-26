from os import name

from playwright.sync_api import Locator, Page
from utils.config import BASE_URL


class HomePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.page_heading: Locator = page.get_by_role(
            "link",
            name="Sign in")
        self.sign_in_link: Locator = page.get_by_role("link", name="Sign In")

    def open(self) -> None:
        self.page.goto(BASE_URL)

    def go_to_login(self) -> None:
        self.sign_in_link.click()

    def get_title(self) -> str:
        return self.page.title


