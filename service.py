def service_charge(amount,customer_type):
    if customer_type.upper() == "VIP":
        return amount
    else:
        return int(amount + (amount * 5/100))
