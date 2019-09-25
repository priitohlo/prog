in_number = int(input("Sisesta arv: "))

cx = 0
cy = 0

for i in range(in_number):
    cx += i + 1
    cy += (i + 1) ** 2
 
cx = cx ** 2

print("Vastus: " + str(cx - cy))