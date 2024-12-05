import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
result = 0

pairs = []
updates = []
with open('Day5-input.txt', 'r') as file:
    firsthalf = True
    for line in file:
        if line == '\n':
            firsthalf = False
        elif firsthalf:
            pairs.append([int(i) for i in line.strip().split('|')])
        else:
            updates.append([int(i) for i in line.strip().split(',')])

for upd in updates:
    is_valid = True
    for i, n in enumerate(upd):
        for pair in pairs:
            if n == pair[1]:
                j = i
                while True:
                    j += 1
                    try:
                        if upd[j] == pair[0]: is_valid = False
                    except IndexError:
                        break
    if is_valid:
        print(upd)
        result += upd[int(len(upd)/2)]

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)