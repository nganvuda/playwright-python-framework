import pytest
from test_data import PRODUCT_NAME
from playwright.sync_api import expect
from utils.config import BASE_URL
from test_data import VALID_USER

@pytest.mark.smoke
def test_add_product_to_cart(home_page) -> None:
    home_page.open()
    home_page.search_product(PRODUCT_NAME)
    product_page = home_page.select_product(PRODUCT_NAME)
    product_page.add_to_cart()
    product_page.header.should_show_cart_count("1")

def test_go_to_checkout(home_page) -> None:
    home_page.open()
    home_page.search_product(PRODUCT_NAME)
    product_page = home_page.select_product(PRODUCT_NAME)
    product_page.add_to_cart()
    checkout_page = product_page.header.go_to_checkout()
    checkout_page.proceed_from_cart()
    expect(checkout_page.page).to_have_url(f"{BASE_URL}checkout")
    checkout_page.form.login(VALID_USER.email, VALID_USER.password)
    checkout_page.proceed_from_signin()
    checkout_page.should_be_on_billing_address_step()
