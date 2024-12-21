import util
import time
util.set_dir("inputs")
start_time = time.time()
result = 0

def factor(input):
    x = findnum(input, ',')
    input = input[len(str(x))+1:]
    y = findnum(input, ')')
    print(f'mul({x},{y})')
    return (x*y)

def findnum(input, delim):
    for i in range(3, -2, -1):
        if input[0:i].isnumeric() and input[i] == delim:
            break
    return 0 if i == -1 else int(input[0:i])

for row in open('Day03-input.txt', 'r'):
    for i, char in enumerate(row):
        if i < 4: continue
        if row[i-4:i] == 'mul(':
            result += factor(row[i:])

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)