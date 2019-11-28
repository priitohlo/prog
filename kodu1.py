def auto_hind(price, years):
    if years == 0:
        return round(price, 2)
    else:
        return auto_hind(price * 0.8, years - 1)