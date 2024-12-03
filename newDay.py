import sys
import os
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]))
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
3
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
''')
    fp.write("for row in open('Day" + str(i) + "-demo.txt', 'r'):\n")
    fp.write('''    a, b = row.split()

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)''')
