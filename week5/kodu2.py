from pykkar import *
import math

def get_input(message, type, max = 0):
    if (type == 'M'):
        while True:
            try:
                inp = int(input(message))
                if (inp % 2) != 0:
                    return inp
                else:
                    raise Exception('notodd')
            except Exception as e:
                t = e.args[0]
                if (t == 'notodd'):
                    print('Peab olema paaritu! Proovime uuesti...')
                else:
                    print('Vigane sisend! Proovime uuesti...')
                pass
    elif (type == 'P'):
        while True:
            try:
                inp = int(input(message))
                if (inp >= max - 1):
                    raise Exception('big')
                elif (inp < 1):
                    raise Exception('small')
                else:
                    return inp
            except Exception as e:
                t = e.args[0]
                if (t == 'big'):
                    print('Liiga suur! Proovime uuesti...')
                elif (t == 'small'):
                    print('Liiga väike! Proovime uuesti...')
                else:
                    print('Vigane sisend! Proovime uuesti...')
                pass
    elif (type == 'D'):
        while True:
            try:
                inp = str(input(message))
                if (inp in ['N', 'E', 'W', 'S', 'n', 'e', 'w', 's']):
                    return inp.upper()
                else:
                    raise Exception()
            except:
                print('Vigane sisend! Proovime uuesti...')
                pass

def generate_world_from_user_input():
    world = ''
    
    directions = {'N': '^', 'E': '>', 'W': '<', 'S': 'v'}

    w = get_input('Sisesta maailma laius: ','M')
    l = get_input('Sisesta maailma kõrgus: ','M')
    x = get_input('Sisesta Pykkari positsiooni x-koordinaat: ', 'P', max = w)
    y = get_input('Sisesta Pykkari positsiooni y-koordinaat: ','P', max = l)
    d = get_input('Sisesta Pykkari suund: ','D')
    
    print(world)


    for i in range(l):
        if i == 0 or i == l-1:
            world += '#' * w + '\n'
        else:
            if i == y:
                world += '#' + ' ' * (x - 1) + directions[d] + ' ' * (w - x - 2) + '#\n'
            else:
                world += '#' + (' ' * (w - 2)) + '#\n'
    
   
    print(world)
    return([world,w,l])


def color_mid():
    
    world, w, l = generate_world_from_user_input()

    create_world(world)

    if get_direction() == 'N':
        for i in range(2):
            right()
    elif get_direction() == 'W':
        for i in range(3):
            right()
    elif get_direction() == 'E':
        right()
    
    while not is_wall():
        step()

    right()

    while not is_wall():
        step()
    
    right()
    
    for i in range(math.ceil((l-3) / 2)):
        step()
    
    right()

    for i in range(math.ceil((w-3) / 2)):
        step()
    
    paint()

    exitonclick()

color_mid()