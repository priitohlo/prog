from pykkar import *
import math

def color_corners(world):
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
    
    for i in range(2):
        right()

    while not is_painted():
        paint()
        while not is_wall():
            step()
        for i in range (3):
            right()
    
    exitonclick()
        
            


world = ("""
########
#  >   #
#      #
#      #
#      #
#      #
########
""")

color_corners(world)