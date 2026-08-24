import pytest
from test_data import PRODUCT_NAME

@pytest.mark.smoke
def test_add_product_to_cart(home_page) -> None:
    home_page.open()
    home_page.search_product(PRODUCT_NAME)
    product_page = home_page.select_product(PRODUCT_NAME)
    product_page.add_to_cart()
    product_page.header.should_show_cart_count("1")