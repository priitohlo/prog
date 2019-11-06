import random

def minu_shuffle(list):
    for i in reversed(range(1, len(list))):
        j = int((i+1) * random.random())
        list[i], list[j] = list[j], list[i]