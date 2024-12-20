import util
import time
import itertools
util.set_dir("inputs")
start_time = time.time()
result = 0

def make_the_math_math(nums, opers, running_total=0):
    if running_total > total: return 0
    if running_total == 0: running_total = nums.pop(0)
    if len(opers):
        match opers.pop(0):
            case '':
                running_total = int(str(running_total) + str(nums.pop(0)))
            case '*':
                running_total = running_total * nums.pop(0)
            case '+':
                running_total = running_total + nums.pop(0)
        return make_the_math_math(nums, opers, running_total)
    else:
        return running_total

# Read the input file 1 row at a time
with open('Day07-input.txt', 'r') as file:
    for line in file:
        total, numbers = line.strip().split(':')
        total = int(total)
        numbers = [int(n) for n in numbers.strip().split()]

        # run thru every permutation of operators. 
        # Start with ops resulting in higher running totals to break out of incorrect loops faster
        for oper_iter in (itertools.product(['','*','+'], repeat=len(numbers)-1)):
            if total == make_the_math_math(numbers.copy(), list(oper_iter)):
                equation = [x for pair in zip([str(n) for n in numbers], oper_iter) for x in pair]
                equation = ''.join(equation)+str(numbers[-1])
                print(total, equation)
                result += total
                break

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)