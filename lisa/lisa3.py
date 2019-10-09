# each block interpreted as a number from 0 through 9
chars = [
# top    
    [   True,
        False,
        True,
        True,
        False,
        True,
        True,
        True,
        True,
        True
    ],
# upper
    [
        [True, True],
        [False, True],
        [False, True],
        [False, True],
        [True, True],
        [True, False],
        [True, False],
        [False, True],
        [True, True],
        [True, True]
    ],
# middle
    [
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        False,
        True,
        True
    ],
# lower
    [
        [True, True],
        [False, True],
        [True, False],
        [False, True],
        [False, True],
        [False, True],
        [True, True],
        [False, True],
        [True, True],
        [False, True]
    ],
# bottom
    [
        True,
        False,
        True,
        True,
        False,
        True,
        True,
        False,
        True,
        True
    ],
]

i_number = input("Sisesta arv: ")
i_length = int(input("Sisesta suurus: "))
space = " "
out = ""

for k, r in enumerate(chars):
    if (k == 0) or (k == 2) or (k == 4):
        for d in i_number:
            out += space
            d = int(d)
            if chars[k][d]:
                out += "-" * i_length
            else:
                out += space * i_length
            out += space + (space * i_length)
        #out = out[:-3]
        out += "\n"
    elif (k == 1) or (k == 3):
        for i in range(i_length):
            for d in i_number:
                d = int(d)
                for s in chars[k][d]:
                    if s:
                        out += "|" + space * i_length
                    else:
                        out += space + space * i_length
            #out = out[:-3]
            out += "\n"

out = out[:-1]
print(out)