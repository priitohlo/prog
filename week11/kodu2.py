def transponeeriK(m):
    retM = [[] for i in range(len(m[0]))]
    m = list(reversed(m))
    
    for i in range(len(m[0])):
        for j in range(len(m)):
            retM[i].append(list(reversed(m[j]))[i])
    
    return(retM)

print(transponeeriK([[11, 12, 13, 14, 15, 16, 17, 18, 19], [21, 22, 23, 24, 25, 26, 27, 28, 29]]))