from playwright.sync_api import expect
from test_data import INVALID_EMAIL, INVALID_PASSWORD


def test_invalid_login(home_page, login_page) -> None:
    home_page.open()
    home_page.go_to_login()
    login_page.login(
        INVALID_EMAIL,
        INVALID_PASSWORD
    )

    login_page.should_show_invalid_credentials_error()
