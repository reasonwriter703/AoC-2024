import sys
import os
import numpy as np
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]))
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )

i = input('Day#?')
with open('inputs/Day' + i + '-demo.txt', 'w') as fp:
    pass
with open('inputs/Day' + i + '-input.txt', 'w') as fp:
    pass
with open('Day' + i + 'a.py', 'w') as fp:
    fp.write('''import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
result = 0

# Option 1 - Read the input file 1 row at a time
''')
    fp.write("for row in open('Day" + str(i) + "-demo.txt', 'r'):\n")
    fp.write('''    a, b = row.split()

# Option 2 - Convert the input into a numpy array
''')
    fp.write("with open('Day" + str(i) + "-demo.txt', 'r') as file:\n")
    fp.write('''    area = np.array([list(line.strip()) for line in file])

for row, line in enumerate(array):
    for col, char in enumerate(line):

             
print('RESULT: ', result)
print('Time taken:', time.time() - start_time)''')