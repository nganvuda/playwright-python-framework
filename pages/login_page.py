from playwright.sync_api import Page
from components.login_form_component import LoginFormComponent
from pages.base_page import BasePage
import logging
logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.form = LoginFormComponent(page)

