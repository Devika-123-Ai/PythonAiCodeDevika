
from Project1_discount import calculate_discount


def main():
    print("=== Retail Customer Service ===")
    print("Project 1: Product Discount Eligibility")

    try:
        cart_total = float(input("Enter cart total: $"))

        #  Validate cart total
        if cart_total < 0:
            print("Error: Invalid cart total")
            return

       
        membership = input(
            "Enter membership (normal/basic/premium): "
        ).strip().lower()

        # Validate membership
        if membership not in ("normal", "basic", "premium"):
            print("Error: Invalid membership")
            return

        
        coupon = input("Valid coupon? (yes/no): ").strip().lower()

        # Validate coupon
        if coupon not in ("yes", "no"):
            print("Please enter yes or no.")
            return

        
        result = calculate_discount(
            cart_total,
            membership,
            coupon == "yes"
        )

        if "error" in result:
            print("Error:", result["error"])
            return

        
        print("\n--- Discount Summary ---")
        print("Membership discount:", result["membership_discount"], "%")
        print("Coupon discount:", result["coupon_discount"], "%")
        print("Applied discount:", result["applied_discount"], "%")
        print("Discount amount: $", result["discount_amount"])
        print("Final total: $", result["final_total"])

    except ValueError:
        print("Invalid cart total. Please enter a number.")


main()