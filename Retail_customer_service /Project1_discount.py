
from config import (
    MINIMUM_SPEND,
    COUPON_DISCOUNT,
    MAX_DISCOUNT,
    MEMBERSHIP_DISCOUNTS
)

def calculate_discount(cart_total, membership, coupon_valid):

    if cart_total < 0:
        return {"error": "Invalid cart total"}

    membership = membership.strip().lower()

    if membership not in MEMBERSHIP_DISCOUNTS:
        return {"error": "Invalid membership"}

    member_discount = MEMBERSHIP_DISCOUNTS[membership]

    coupon_discount = 0

    if coupon_valid and cart_total >= MINIMUM_SPEND:
        coupon_discount = COUPON_DISCOUNT

    total_discount = member_discount + coupon_discount

    applied_discount = min(total_discount, MAX_DISCOUNT)

    discount_amount = cart_total * applied_discount / 100

    final_total = cart_total - discount_amount

    return {
        "membership_discount": member_discount,
        "coupon_discount": coupon_discount,
        "applied_discount": applied_discount,
        "discount_amount": discount_amount,
        "final_total": final_total
    }