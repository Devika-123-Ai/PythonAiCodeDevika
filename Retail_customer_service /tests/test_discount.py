
import pytest
from Project1_discount import calculate_discount


# Positive and boundary test cases
@pytest.mark.parametrize(
    "cart,membership,coupon,expected",
    [
        (200, "normal", False, 200.0),     # TC01
        (200, "basic", False, 190.0),      # TC02
        (200, "premium", False, 180.0),    # TC03
        (200, "normal", True, 180.0),      # TC04
        (200, "basic", True, 170.0),       # TC05
        (200, "premium", True, 160.0),     # TC06
        (99, "normal", True, 99.0),        # TC07
        (100, "normal", True, 90.0),       # TC08
        (200, "BASIC", False, 190.0),      # TC13
        (200, " premium ", False, 180.0),  # TC14
        (0, "normal", False, 0.0)          # TC15
    ]
)
def test_discount(cart, membership, coupon, expected):
    result = calculate_discount(cart, membership, coupon)
    assert result["final_total"] == expected


# TC09: Negative cart
def test_negative_cart():
    result = calculate_discount(-100, "basic", True)
    assert result["error"] == "Invalid cart total"


# TC10: Invalid membership
def test_invalid_membership():
    result = calculate_discount(200, "vip", True)
    assert result["error"] == "Invalid membership"


# TC11: Invalid coupon
# This validation is handled by main.py, not calculate_discount().


# TC12: Invalid cart input
# This validation is handled by main.py, not calculate_discount().
