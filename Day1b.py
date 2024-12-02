import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

result = 0
list_x = []
list_y = []
for row in open('Day1-input.txt', 'r'):
    x, y = row.strip().split('   ')
    list_x.append(int(x))
    list_y.append(int(y))

for id_x in list_x:
    count = 0
    for id_y in list_y:
        if id_x == id_y:
            count += 1
    result += (id_x * count)

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)