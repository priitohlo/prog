name = ''
price = -1.0

distance = float(input("Sisesta tee pikkus kilomeetrites: "))

with open("week6/taksohinnad.txt", "r") as f:
    for r in f:
        taxi = r.split(",")
        if ((float(taxi[1]) + distance * float(taxi[2])) < price) and price != -1.0:
            price = float(taxi[1]) + distance * float(taxi[2])
            name = taxi[0]
        elif (price == -1.0):
            price = float(taxi[1]) + distance * float(taxi[2])
            name = taxi[0]

        print(price)

print("Kõige odavam on " + name)