def gst(amount):
    Gst = amount + (amount * 18/100)
    if amount > 4000:
        return Gst + (Gst * 5/100)
    else:
        return Gst
