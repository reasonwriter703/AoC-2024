import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

import re
result = 0
list_x = []
list_y = []
for row in open('Day1-input.txt', 'r'):
    x, y = row.strip().split('   ')
    list_x.append(int(x))
    list_y.append(int(y))
list_x = sorted(list_x)
list_y = sorted(list_y)

print(list_x, list_y)
for i in range(len(list_x)):
    if list_x[i] > list_y[i]:
        dist = list_x[i] - list_y[i]
    else:
        dist = list_y[i] - list_x[i]
    print(list_x[i], list_y[i], result)
    result += dist

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)