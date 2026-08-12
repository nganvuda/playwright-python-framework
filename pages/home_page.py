from playwright.sync_api import Page
from components.header_component import HeaderComponent
from pages.login_page import LoginPage
from utils.config import BASE_URL
from pages.base_page import BasePage
import logging
logger = logging.getLogger(__name__)


class HomePage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.header = HeaderComponent(page)

    def open(self) -> None:
        logger.info(f"Opening Home Page: {BASE_URL}")
        self.page.goto(BASE_URL)

    def go_to_login(self) -> LoginPage:
        logger.info("Going to Login Page")
        self.header.click_sign_in()
        return LoginPage(self.page)

