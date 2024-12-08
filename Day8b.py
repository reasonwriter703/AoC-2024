import sys
import os
import time
import numpy as np
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
result = 0

def move(this_tpl, new_tpl, steps=1):
    if steps != 1:
        x_tpl = tuple(i * steps for i in new_tpl)
        return tuple(map(lambda i, j: i + j, this_tpl, x_tpl))
    else:
        return tuple(map(lambda i, j: i + j, this_tpl, new_tpl))

def out_of_bounds(area, coord):
    if coord[0] < 0 or coord[1] < 0: return True
    try:
        xy = area[coord]
        return False
    except IndexError:
        return True

# Convert the input into a numpy array
with open('Day8-input.txt', 'r') as file:
    area = np.array([list(line.strip()) for line in file])
antinodes = (area == '#')    #boolean mask

for this_y, line in enumerate(area):
    for this_x, char in enumerate(line):
        if char == '.': continue
        this_coord = (this_y, this_x)
        matches = np.where(area == char)
        for y, x in zip(matches[0], matches[1]):
            if y == this_y and x == this_x: continue    #skip the current antenna
            dist = tuple(map(lambda i, j: (i - j), (y, x), this_coord))
            i = 1
            while True:
                new_anti = move(this_coord, dist, i)
                if out_of_bounds(area, new_anti): break
                antinodes[new_anti] = True
                i += 1
                
print('RESULT: ', antinodes.sum())
print('Time taken:', time.time() - start_time)