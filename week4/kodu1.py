c = 299792.458

def summa(u, v):
    return (u + v) / (1 + ((u * v) / (c ** 2)))

texts = ['Esimese keha kiirus vaatleja suhtes on: ',
'Teise keha kiirus esimese keha suhtes on: ',
'Kolmanda keha kiirus teise keha suhtes on: ',
'Neljanda keha kiirus kolmanda keha suhtes on: ']
s = 0.0
u = 0.0
v = 0.0

for i in range(4):
    if i == 0:
        u = float(input(texts[i]))
    elif i > 0:
        v = float(input(texts[i]))
        d = summa(u,v)
        s += summa(u,v)
        u = v

print('Kiiruste summa on: ' + str(s))