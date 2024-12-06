import sys
import os
import time
import numpy as np
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
result = 0


# Convert the input into a 2D array
with open('Day6-input.txt', 'r') as file:
    area = np.array([list(line.strip()) for line in file])
obstruction = (area == 'n/a')
compass = {0:'N', 1:'E', 2:'S', 3:'W'}
facing = 0

for row, line in enumerate(area):
    for col, char in enumerate(line):
        if char != '.': continue
        new_area = area.copy()
        new_area[row][col] = '#'    #place obstruction
        visited = (area == '^') #reset bool mask

        last_patrolled = 0
        while True:
            guard = np.where(new_area == '^')
            visited[guard] = True
            up = int(guard[0]-1), guard[1]
            if int(up[0]) < 0:
                break
            if new_area[up] == '.': #walk
                new_area[guard], new_area[up] = new_area[up], new_area[guard]
                
                
            else: #turn
                new_area = np.rot90(new_area)
                visited = np.rot90(visited)
                facing = 0 if facing == 3 else facing + 1
                if facing == 0: 
                    if last_patrolled == visited.sum():
                        #guard is stuck!
                        obstruction[row][col] = True
                        print(row, col, 'True')
                        break
                    last_patrolled = visited.sum()

print('RESULT: ', obstruction.sum())
print('Time taken:', time.time() - start_time)