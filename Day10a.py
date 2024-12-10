import util
import time
import numpy as np
util.set_dir("inputs")
start_time = time.time()
result = 0

def take_a_hike(area, coord, behind_you=None):
    height = area[coord]
    for compass_i, dir in enumerate(util.compass):
        # try:
        #     if dir[compass_i] == dir[behind_you]: continue #skip the direction you came from
        # except:
        #     pass
        coord_next = util.move_coords(coord, dir)
        if (util.out_of_bounds(area, coord_next) == False
        and area[coord_next] == height + 1): 
            if area[coord_next] == 9:
                global summits
                summits.add(coord_next)
            else:
                take_a_hike(area, coord_next, compass_i - 2)

# Convert the input into a numpy array
with open('Day10-input.txt', 'r') as file:
    area = np.array([[int(n) for n in line.strip()] for line in file])

trailheads = []
for this_y, line in enumerate(area):
    for this_x, char in enumerate(line):
        if char == 0:
            summits = set()
            take_a_hike(area, (this_y, this_x))
            trailheads.append(summits)

print(trailheads)
for t in trailheads:
    result += len(t)
print('RESULT: ', result)
print('Time taken:', time.time() - start_time)