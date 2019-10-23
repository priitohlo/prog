def arvutaHinnad(prices, markup):
    for k, v in enumerate(prices):
        prices[k] = v * (1 + markup/100) * 1.2
    return prices