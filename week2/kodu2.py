import math

def posts(cable_length, max_distance):
    return int(math.ceil(cable_length / max_distance + 1))

in_cable_length = int(input('Sisesta liini pikkus: '))
in_max_distance = int(input('Sisesta liini pikkus: '))

print(posts(in_cable_length, in_max_distance))