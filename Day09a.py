import util
import time
util.set_dir("inputs")
start_time = time.time()
result = 0
disk_map = []

# Read the input file 1 row at a time
for row in open('Day09-input.txt', 'r'):
    for i, char in enumerate(row):
        char = int(char)
        fileID = int(i/2)
        for c in range(char):
            disk_map.append(fileID if i % 2 == 0 else '.')

open_blocks = 0
next_open = 0
while True:
    if disk_map[-1] == '.':
        disk_map.pop()
        open_blocks += 1
    else:
        while True:
            if disk_map[next_open] == '.':
                disk_map[next_open] = disk_map[-1]
                disk_map.pop()
                open_blocks += 1
                break
            next_open += 1

    if '.' not in disk_map: break

for i, n in enumerate(disk_map):
    result += i * int(n)

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)