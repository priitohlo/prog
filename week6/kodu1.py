def poisse_ja_tüdrukuid(l):
    b = 0
    g = 0
    
    for n in l:
        if n[-1:] == 'P':
            b += 1
        elif n[-1:] == 'T':
            g += 1
    
    return b,g