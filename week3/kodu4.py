f = open("week3/pikkused.txt", "r")

for r in f:
    try:
        o = round(3 / 2 * float(r.strip()) + 2)
        print(str(o))
    except:
        print("Vigane sisend")