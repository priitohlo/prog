from math import pi

cakes = {'šokolaadikook': ['r', .05], 
            'maasikakook': ['r', .04], 
            'Napoleoni kook': ['s', .08]}

def koogi_hind(n, m):
    if n in cakes:
        if cakes[n][0] == 'r':
            return round(pi * m ** 2 * cakes[n][1], 2)
        elif cakes[n][0] == 's':
            return round(m ** 2 * cakes[n][1], 2)
    else:
        raise Exception('Sellist kooki andmebaasist ei leitud')