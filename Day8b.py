import util
import time
import numpy as np
util.set_dir("inputs")
start_time = time.time()
result = 0

# Convert the input into a numpy array
with open('Day8-input.txt', 'r') as file:
    area = np.array([list(line.strip()) for line in file])
antinodes = (area == '#')    #boolean mask

for this_y, line in enumerate(area):
    for this_x, char in enumerate(line):
        if char == '.': continue
        this_coord = (this_y, this_x)   #create tuple of this antenna's coordinates
        matches = np.where(area == char)    #get list of coordinates of matching antennas
        for y, x in zip(matches[0], matches[1]):
            if y == this_y and x == this_x: continue    #skip the current antenna
            dist = tuple(map(lambda i, j: (i - j), (y, x), this_coord)) #get distance between antennas
            i = 1
            while True:
                new_anti = util.move_coords(this_coord, dist, i)    #add an antinode along each point on the line until out of bounds
                if util.out_of_bounds(area, new_anti): break
                antinodes[new_anti] = True
                i += 1
                
print('RESULT: ', antinodes.sum())
print('Time taken:', time.time() - start_time)