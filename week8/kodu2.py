from random import sample

def bingo():
    while True:
        numbers = sample(range(1, 10), 3) + sample(range(11, 20), 2)
        if not (1 in numbers and 2 in numbers and 3 in numbers):
            break
    return numbers

print(bingo())