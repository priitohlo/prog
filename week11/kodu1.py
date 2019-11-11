def seosta_lapsed_ja_vanemad(fc, fn):
    names = {}
    children = {}

    with open(fn, 'r') as f:
        for r in f:
            r = r.split(' ')
            names[r[0]] = r[1] + ' ' + r[2].strip()
    
    with open(fc, 'r') as f:
        for r in f:
            r = r.split(' ')
            p = names[r[1].strip()]
            n = names[r[0]]
            if p in children:
                children[p].add(n)
            else:
                children[p] = {n}
    
    return children


print(seosta_lapsed_ja_vanemad('week11/lapsed.txt', 'week11/nimed.txt'))