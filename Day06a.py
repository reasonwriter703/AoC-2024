import util
import time
import numpy as np
util.set_dir("inputs")
start_time = time.time()
result = 0

# Convert the input into a 2D array
with open('Day06-input.txt', 'r') as file:
    area = np.array([list(line.strip()) for line in file])
visited = (area == '^') #create bool mask

while True:
    guard = np.where(area == '^')
    visited[guard] = True
    up = int(guard[0]-1), guard[1]
    if int(up[0]) < 0: break
    try:
        if area[up] == '.': #walk
            area[guard], area[up] = area[up], area[guard]
            
        else: #turn
            area = np.rot90(area)
            visited = np.rot90(visited)
    except IndexError:
        break

print(visited)
print('RESULT: ', visited.sum())
print('Time taken:', time.time() - start_time)