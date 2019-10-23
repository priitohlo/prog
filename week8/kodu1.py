def loetleReisid(file, budget):
    possibleTrips = []
    with open(file, 'r') as f:
        for r in f:
            r = r.split(';')
            if int(r[1].strip()) <= budget:
                possibleTrips.append(r[0])
    return possibleTrips

print(loetleReisid('week8/reisid.txt', int(input('Sisesta sobiv reisi eelarve: '))))