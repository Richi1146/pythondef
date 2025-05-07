import string
import random

# 1. Shopping cart simulator
def calculate_cart_total(cart, iva=0.21):
    total = sum(item['price'] * item['quantity'] for item in cart)
    total_with_iva = total * (1 + iva)
    return total_with_iva

cart = [
        {"name": "Shirt", "price": 20.0, "quantity": 2},
        {"name": "Pants", "price": 40.0, "quantity": 1}
    ]
total_price = calculate_cart_total(cart)
print(total_price)

# 2. Text processing (word count)


# 3. Secure password generator


# 4. Weather analyzer (temperatures)


# 5. Functional contact book
