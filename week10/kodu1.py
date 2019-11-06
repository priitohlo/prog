def erinevad_sümbolid(s):
    return set(s)


def sümbolite_sagedus(s):
    retDict = {}
    symbols = erinevad_sümbolid(s)
    for e in symbols:
        retDict[e] = s.count(e)
    return retDict

def grupeeri(s):
    retDict = {}
    symbol_freq = sümbolite_sagedus(s)
    retDict['Täishäälikud'] = set()
    retDict['Kaashäälikud'] = set()
    retDict['Muud'] = set()
    for k, v in symbol_freq.items():
        if k in 'aeiouõäöüAEIOUÕÄÖÜ':
            retDict['Täishäälikud'].add((k,v))
        elif k in 'bcdfghjklmnpqrsšzžtvwxyzBCDFGHJKLMPQRSŠZŽTVWXYZ':
            retDict['Kaashäälikud'].add((k,v))
        else:
            retDict['Muud'].add((k,v))
    return retDict



print(grupeeri("sõida tasa üle silla"))