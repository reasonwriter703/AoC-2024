import sys
import os
def set_dir(subfolderpath):
    working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + '/' + subfolderpath)
    if len(sys.argv) > 1: working = sys.argv[1]
    os.chdir( working )

compass = [(-1,0), (0,1), (1,0), (0,-1)]    #N, E, S, W
compass8 = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]    #N, NE, E, SE, S, SW, W, NW
def move_coords(this_tpl, new_tpl, steps=1):
    if steps != 1:
        x_tpl = tuple(i * steps for i in new_tpl)
        return tuple(map(lambda i, j: i + j, this_tpl, x_tpl))
    else:
        return tuple(map(lambda i, j: i + j, this_tpl, new_tpl))

def turn_r(facing):
    try:
        return compass[facing + 1]
    except IndexError:
        return compass[0]

def turn_l(facing):
    return compass[facing - 1]

def out_of_bounds(area, coord):
    if coord[0] < 0 or coord[1] < 0: return True
    try:
        xy = area[coord]
        return False
    except TypeError:
        try:
            xy = area[coord[0]][coord[1]]
        except IndexError:
            return True
    except IndexError:
        return True