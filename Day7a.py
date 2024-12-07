import sys
import os
import time
import itertools
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()

result = 0

# Convert the input into a 2D array
with open('Day7-input.txt', 'r') as file:
    for line in file:
        total, numbers = line.strip().split(':')
        total = int(total)
        numbers = [(n) for n in numbers.strip().split()]
        opercombo = list(itertools.product(['+','*'], repeat=len(numbers)-1))
        for c in opercombo:
            for i, n in enumerate(numbers):
                if i == 0: 
                    running_total = int(n)
                else:
                    equ = str(running_total)+c[i-1]+n
                    running_total = eval(equ)
            if running_total == total:
                result += total
                break
    
print('RESULT: ', result)
print('Time taken:', time.time() - start_time)