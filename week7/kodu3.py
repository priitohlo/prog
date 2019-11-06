import math

months = ['jaanuar', 
            'veebruar', 
            'märts', 
            'aprill', 
            'mai', 
            'juuni', 
            'juuli', 
            'august', 
            'september', 
            'oktoober', 
            'november', 
            'detsember']

def sünnikuupäev(idcode):
    return idcode[5:7] + '. ' + months[int(idcode[3:5]) - 1] + ' ' + str(1800 + (math.ceil(int(idcode[0]) / 2) - 1) * 100 + int(idcode[1:3]))