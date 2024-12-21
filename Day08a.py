import util
import time
import numpy as np
util.set_dir("inputs")
start_time = time.time()
result = 0

# Convert the input into a numpy array
with open('Day08-input.txt', 'r') as file:
    area = np.array([list(line.strip()) for line in file])
antinodes = (area == '#')    #boolean mask

for this_y, line in enumerate(area):
    for this_x, char in enumerate(line):
        if char == '.': continue
        this_coord = (this_y, this_x)
        matches = np.where(area == char)
        for y, x in zip(matches[0], matches[1]):
            if y == this_y and x == this_x: continue    #skip the current antenna
            dist = tuple(map(lambda i, j: (i - j) * 2, (y, x), this_coord))
            dist = util.move_coords(this_coord, dist)
            if not util.out_of_bounds(area, dist):
                antinodes[dist] = True


print('RESULT: ', antinodes.sum())
print('Time taken:', time.time() - start_time)