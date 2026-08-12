import pytest
from playwright.sync_api import expect
from test_data import INVALID_USER

@pytest.mark.smoke
def test_invalid_login(home_page) -> None:
    home_page.open()
    login_page = home_page.go_to_login()
    login_page.login(
        INVALID_USER.email,
        INVALID_USER.password,
    )
    login_page.should_show_invalid_credentials_error()
