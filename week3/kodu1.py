def pretax_income(income):
    if income < 6000:
        r = income
    elif income >= 6000 and income < 14400:
        r = 6000
    elif income >= 14400 and income < 25200:
        r = 6000 - 6000 / 10800 * (income - 14400)
    elif income >= 25200:
        r = 0
    
    return round(r, 2)

in_income = float(input("Sisesta aastatulu: "))

print(pretax_income(in_income))