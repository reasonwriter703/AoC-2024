import util
import time
import numpy as np
util.set_dir("inputs")
start_time = time.time()
result = 0

def patrol(area, check_if_stuck=False):
    coord_guard = guard_start
    facing = 0  #north
    last_patrolled = 0
    while True:
        coord_next = util.move(coord_guard, util.compass[facing])
        if util.out_of_bounds(area, coord_next): 
            break
        elif area[coord_next] != '#': #walk
            coord_guard = coord_next
            area[coord_guard] = '^'

        else: #turn_r
            facing = 0 if facing == 3 else facing + 1
            if check_if_stuck and (facing == 0): 
                patrolled = (area == '^').sum()
                if last_patrolled == patrolled:
                    #guard is stuck!
                    obstruction[row][col] = True
                    print(row, col, 'True')
                    break
                last_patrolled = patrolled
    return area

# Convert the input into a 2D array
with open('Day6-input.txt', 'r') as file:
    area = np.array([list(line.strip()) for line in file])
guard_start = np.where(area == '^')

true_area = patrol(area.copy())      #original timeline

obstruction = (area == 'n/a')
for row, line in enumerate(area):
    for col, char in enumerate(line):
        if true_area[row][col] != '^': continue     #if obstruction doesn't touch guard's original patrol, ignore
        if char != '.': continue
        new_area = area.copy()      #new timeline
        new_area[row][col] = '#'    #place obstruction
        patrol(new_area, True)

print('RESULT: ', obstruction.sum())
print('Time taken:', time.time() - start_time)