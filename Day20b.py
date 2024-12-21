import util
import time
from collections import deque
util.set_dir("inputs")
start_time = time.time()
phase_max = 20   #2 for part 1, 20 for part 2

def runmaze(area, start):
    queue = deque([start])
    parent = {}
    while queue:
        coord = queue.popleft()
        if coord == (end_r, end_c):   #finished maze
            # return area[coord[0]][coord[1]]
            path = []
            while coord != start:
                path.append(coord)
                coord = parent[coord]
            path.append(start)
            path.reverse()
            return path
        
        for step in util.compass:
            nr, nc = util.move_coords(coord, step)
            if util.out_of_bounds(area, (nr, nc)): continue
            if area[nr][nc] != '.': continue
            queue.append((nr, nc))
            parent[(nr, nc)] = coord
            area[nr][nc] = area[coord[0]][coord[1]] + 1

    return None #no path found


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

honest_path = runmaze(maze, (start_r, start_c))      #no cheats
honest_runtime = len(honest_path) - 1

cheats = {}
for i, phase_in in enumerate(honest_path):
    # print(len(honest_path) - i)
    
    #get map of phase range
    for offset_r in range(-phase_max, phase_max + 1):
        for offset_c in range(-phase_max, phase_max + 1):
            phase_len = abs(offset_r) + abs(offset_c)
            if phase_len > phase_max or phase_len <= 1 : continue   #skip if out of range or in normal step range
            phase_out = util.move_coords(phase_in, (offset_r, offset_c))
            if util.out_of_bounds(maze, phase_out): continue
            try:
                steps = int(maze[phase_out[0]][phase_out[1]])
            except ValueError:
                continue
            steps = steps - phase_len - i  #number of picos saved
            if steps >= 100:   #if at least 100 picos were saved
                if steps not in cheats:
                    cheats[steps] = 1
                else:
                    cheats[steps] += 1

cheats = dict(sorted(cheats.items()))
for c in cheats:
    print(f"There are {cheats[c]} cheats that save {c} picos.")

print('RESULT: ', sum(cheats.values()))
print('Time taken:', time.time() - start_time)