import util
import time
import copy
from collections import deque
util.set_dir("inputs")
start_time = time.time()

def runmaze(area):
    queue = deque([(start_r, start_c)])
    while queue:
        coord = queue.popleft()

        if coord == (end_r, end_c):   #finished maze
            return area[coord[0]][coord[1]]

        for step in util.compass:
            nr, nc = util.move_coords(coord, step)
            if util.out_of_bounds(area, (nr, nc)): continue
            if area[nr][nc] != '.': continue
            queue.append((nr, nc))
            area[nr][nc] = area[coord[0]][coord[1]] + 1

    return None

# Convert the input into a 2D array
maze = []
with open('Day20-input.txt', 'r') as file:
    for row, line in enumerate(file):
        maze.append(list(line.strip()))
        for col, char in enumerate(line):
            match char:
                case 'S':
                    start_r = row
                    start_c = col
                case 'E':
                    end_r = row
                    end_c = col

maze[start_r][start_c] = 0
maze[end_r][end_c] = '.'

honest_runtime = runmaze(copy.deepcopy(maze))      #no cheats

cheats = {}
for row, line in enumerate(maze):
    print(len(maze) - row)
    for col, char in enumerate(line):
        if (char != '#'
        or row == 0
        or col == 0
        or row == len(maze)
        or col == len(maze[0])): continue   #skip pointless cheats
        new_area = copy.deepcopy(maze)      #new cheat
        new_area[row][col] = '.'    #phase thru wall
        newtime = runmaze(new_area)
        if newtime + 100 <= honest_runtime:
            newtime = honest_runtime - newtime   #keep number of picos saved
            if newtime not in cheats:
                cheats[newtime] = 1
            else:
                cheats[newtime] += 1
cheats = dict(sorted(cheats.items()))

print('RESULT: ', sum(cheats.values()))
print('Time taken:', time.time() - start_time)