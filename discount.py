def apply_discount(total_amount, total_quantity, customer_type):

    discount_amount = 0

    # Bill Based Discount
    if total_amount >= 5000:
        discount_amount += total_amount * 0.20
    elif total_amount >= 3000:
        discount_amount += total_amount * 0.15
    elif total_amount >= 2000:
        discount_amount += total_amount * 0.10
    elif total_amount >= 1000:
        discount_amount += total_amount * 0.05

    # Quantity Based Bonus
    if total_quantity >= 15:
        discount_amount += 200
    elif total_quantity >= 10:
        discount_amount += 100

    # VIP Discount
    if customer_type.upper() == "VIP":
        discount_amount += total_amount * 0.05

    return discount_amount
