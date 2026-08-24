from playwright.sync_api import Page
from components.header_component import HeaderComponent

class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.header = HeaderComponent(page)

    def get_title(self) -> str:
        return self.page.title()

    def refresh(self) -> None:
        return self.page.reload()