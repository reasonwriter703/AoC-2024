i = input('Day#?')
i = '0' + str(i) if i < 10 else str(i)
with open('inputs/Day' + i + '-demo.txt', 'w') as fp:
    pass
with open('inputs/Day' + i + '-input.txt', 'w') as fp:
    pass
with open('Day' + i + 'a.py', 'w') as fp:
    fp.write('''import util
import time
import numpy as np
util.set_dir("inputs")
start_time = time.time()
result = 0

# Option 1
# Read the input file 1 row at a time
''')
    fp.write("for row in open('Day" + i + "-demo.txt', 'r'):\n")
    fp.write('''    a, b = row.split()

# Option 2
# Convert the input into a numpy array
''')
    fp.write("with open('Day" + i + "-demo.txt', 'r') as file:\n")
    fp.write('''    area = np.array([list(line.strip()) for line in file])

for row, line in enumerate(area):
    for col, char in enumerate(line):

             
print('RESULT: ', result)
print('Time taken:', time.time() - start_time)''')