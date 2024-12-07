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
        opercombo = list(itertools.product(['+','*',''], repeat=len(numbers)-1))
        for c in opercombo:
            running_total = int(numbers[0])
            for i, op in enumerate(c):
                equ = str(running_total)+op+numbers[i+1]
                running_total = eval(equ)
                if running_total > total: break
            
            if running_total == total:
                equation = [x for pair in zip(numbers, c) for x in pair]
                equation = ''.join(equation)+numbers[-1]
                print(total, equation)
                result += total
                break

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)