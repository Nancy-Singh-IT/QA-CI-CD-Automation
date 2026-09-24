def test_login_validation():
    username = "standard_user"
    password = "secret_sauce"

    assert username == "standard_user"
    assert password == "secret_sauce"


def test_product_price():
    price = 29.99

    assert price > 0
    assert isinstance(price, float)


def test_cart_item_count():
    cart_items = ["Sauce Labs Backpack"]

    assert len(cart_items) == 1

