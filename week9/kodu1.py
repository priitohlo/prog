from statistics import mean
import matplotlib.pyplot as plot

def silu_andmed(numbers, integer):
    slice_from = 0
    retList = []
    for slice_to in range(1, len(numbers) + 1):
        if (slice_to - slice_from) > integer:
            slice_from += 1
        retList.append(mean(numbers[slice_from:slice_to]))
    return retList
        
x = [1, 3, 2, 4, 3, 5]
print(silu_andmed(x, 3))

data = []

with open(input("Sisesta failinimi: "), "r") as f:
    for r in f:
        r = r.split(", ")
        data.append(float(r[1].strip()))

data_normalised = silu_andmed(data, 50)

fig = plot.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(data)
ax.plot(data_normalised)
ax.set_xlabel("aktsiad")

plot.show()