from maze_generator import Maze
from pykkar import *

debug = input("režiimi valikuks siseta silumine või tava: ")

oMaze = Maze(11, 11)
world = oMaze.text_maze()
create_world(world)
set_speed(10)

while not is_box():
    right()
    print(get_direction()) if debug == "silumine" else True
    if is_wall():
        right()
        print(get_direction()) if debug == "silumine" else True
        right()
        print(get_direction()) if debug == "silumine" else True
        right()
        print(get_direction()) if debug == "silumine" else True
        if is_wall():
            right()
            print(get_direction()) if debug == "silumine" else True
            right()
            print(get_direction()) if debug == "silumine" else True
            right()
            print(get_direction()) if debug == "silumine" else True
            if is_wall():
                right()
                print(get_direction()) if debug == "silumine" else True
                right()
                print(get_direction()) if debug == "silumine" else True
                right()
                print(get_direction()) if debug == "silumine" else True
                paint()
                step()
                print(str(get_x()) + ', ' + str(get_y())) if debug == "silumine" else True
        elif not is_box():
            paint()
            step()
            print(str(get_x()) + ', ' + str(get_y())) if debug == "silumine" else True
    elif not is_box():
        paint()
        step()
        print(str(get_x()) + ', ' + str(get_y())) if debug == "silumine" else True

exitonclick()