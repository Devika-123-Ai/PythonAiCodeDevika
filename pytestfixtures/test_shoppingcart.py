#Assignment 3: Shopping Cart Fixture
#Create a fixture returning Laptop, Mouse, and Keyboard with prices. Write tests for product count,
#product existence, and total price.

import pytest

@pytest.fixture
def shoppingcart():
    return {
        "Laptop": 10000,
        "Mouse": 500,
        "Keyboard": 1000
    }


def test_productcount(shoppingcart):
    assert len(shoppingcart) == 3


def test_product_exists(shoppingcart):
    assert "Laptop" in shoppingcart     #verifying product exist
    assert "Mouse" in shoppingcart
    assert "Keyboard" in shoppingcart


def test_total_price(shoppingcart):
    total=shoppingcart["Laptop"] + shoppingcart["Mouse"] + shoppingcart["Keyboard"]

    assert total==11500