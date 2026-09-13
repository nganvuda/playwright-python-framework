import pytest
from test_data import PRODUCT_NAME, TEST_ADDRESS, VALID_USER


@pytest.mark.smoke
def test_add_product_to_cart(home_page) -> None:
    home_page.open()
    home_page.search_product(PRODUCT_NAME)
    product_page = home_page.select_product(PRODUCT_NAME)
    product_page.add_to_cart()
    product_page.header.should_show_cart_count("1")

@pytest.fixture
def checkout_at_billing_address(home_page):
    home_page.open()
    home_page.search_product(PRODUCT_NAME)
    product_page = home_page.select_product(PRODUCT_NAME)
    product_page.add_to_cart()
    checkout_page = product_page.header.go_to_checkout()
    checkout_page.proceed_from_cart()
    checkout_page.form.login(VALID_USER.email, VALID_USER.password)
    checkout_page.proceed_from_signin()
    checkout_page.should_be_on_billing_address_step()
    return checkout_page

def test_complete_purchase(checkout_at_billing_address) -> None:
    checkout_page = checkout_at_billing_address
    checkout_page.fill_billing_address(TEST_ADDRESS)
    checkout_page.proceed_from_address()
    checkout_page.complete_payment_with_cash_on_delivery()
    checkout_page.should_show_payment_successfully()
