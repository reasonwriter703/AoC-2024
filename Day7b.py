import sys
import os
import time
import itertools
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
result = 0

def make_the_math_math(nums, opers, running_total=0):
    if running_total > total: return 0
    if running_total == 0: running_total = nums.pop(0)
    if len(opers):
        return make_the_math_math(nums, opers, eval(str(running_total)+opers.pop(0)+str(nums.pop(0))))
    else:
        return running_total

# Read the input file 1 row at a time
with open('Day7-input.txt', 'r') as file:
    for line in file:
        total, numbers = line.strip().split(':')
        total = int(total)
        numbers = [n for n in numbers.strip().split()]

        # run thru every permutation of operators. 
        # Start with ops resulting in higher running totals to break out of incorrect loops faster
        for oper_iter in (itertools.product(['','*','+'], repeat=len(numbers)-1)):
            if total == make_the_math_math(numbers.copy(), list(oper_iter)):
                equation = [x for pair in zip(numbers, oper_iter) for x in pair]
                equation = ''.join(equation)+numbers[-1]
                print(total, equation)
                result += total
                break

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)