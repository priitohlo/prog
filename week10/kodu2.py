def võitja(m):
    retDict = {'O': 0, 'X': 0}
        
    for k in retDict:
        for x in range(len(m[0])):
            for y in range(len(m[0])):
                try:
                    if m[x][y] == k and m[x][y+1] == k and m[x][y+2] == k:
                        retDict[k] += 1
                except IndexError:
                    pass
                try:
                    if m[x][y] == k and m[x+1][y] == k and m[x+2][y] == k:
                        retDict[k] += 1
                except IndexError:
                    pass
                try:
                    if m[x][y] == k and m[x+1][y+1] == k and m[x+2][y+2] == k:
                        retDict[k] += 1
                except IndexError:
                    pass
                try:
                    if (y - 1 < 0) or (y - 2 < 0):
                        raise IndexError
                    if m[x][y] == k and m[x+1][y-1] == k and m[x+2][y-2] == k:
                        retDict[k] += 1
                except IndexError:
                    pass
    return retDict

print(võitja([['O',' ','O','X'],
              ['O','O','X','X'],
              ['O','X','O',' '],
              ['X','X','X','O']]))