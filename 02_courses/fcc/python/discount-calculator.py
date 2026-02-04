# 1. You should have a function named apply_discount.
# 2. Your apply_discount function should take two parameters: price and discount.

def apply_discount(price, discount):
    if isinstance(price, (int, float)) and isinstance(discount, (int, float)):
        print(price - (price * discount / 100))
    elif not isinstance(discount, int) or not isinstance(discount, float):
        print("Discount needs to be a number")
    elif not isinstance(price, int) or not isinstance(price, float):
        print("Price needs to be a number")


# 3. When apply_discount is called with a price (first argument) that is not a number (int or float) it should return The price should be a number.
# 4. When apply_discount is called with a discount (second argument) that is not a number (int or float) it should return The discount should be a number.
# 5. When apply_discount is called with a price lower than or equal to 0, it should return The price should be greater than 0.
# 6. When apply_discount is called with a discount lower than 0 or greater than 100, it should return The discount should be between 0 and 100.
# 7. apply_discount(100, 20) should return 80.
# 8. apply_discount(200, 50) should return 100.
# 9. apply_discount(50, 0) should return 50.
# 10. When apply_discount is called with a discount of 100, it should return 0.
# 11. apply_discount(74.5, 20.0) should return 59.6.

apply_discount(100, 100)
apply_discount(50, "time")
apply_discount("time", 50)
