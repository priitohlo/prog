def translate(infile, outfile):
    fo = open(outfile, 'w')

    i = 0
    with open(infile, 'r') as fi:
        for r in fi:
            if r.find('Hello') > -1:
                i += r.count('Hello')
                fo.write(r.replace('Hello', 'Tere'))
    
    return i

in_infile = input('Lähtefaili nimi: ')
in_outfile = input('Sihtfaili nimi: ')

print(translate(in_infile, in_outfile))