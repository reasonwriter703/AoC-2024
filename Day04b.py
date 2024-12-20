import util
import time
util.set_dir("inputs")
start_time = time.time()
result = 0

# Read the text file and convert it into a 2D array
with open('Day04-input.txt', 'r') as file:
    array = [list(line.strip()) for line in file]

for row, line in enumerate(array):
    if row == 0 or row == len(array)-1:
        continue
    for col, char in enumerate(line):
        if col == 0 or col == len(line)-1:
            continue
        if array[row][col] == 'A':
            #NORTH Ms
            if (array[row-1][col+1] == 'M' and array[row-1][col-1] == 'M' and 
            array[row+1][col+1] == 'S' and array[row+1][col-1] == 'S'):
                result += 1

            #SOUTH Ms
            if (array[row+1][col+1] == 'M' and array[row+1][col-1] == 'M' and 
            array[row-1][col+1] == 'S' and array[row-1][col-1] == 'S'):
                result += 1
            
            #WEST Ms
            if (array[row+1][col-1] == 'M' and array[row-1][col-1] == 'M' and 
            array[row+1][col+1] == 'S' and array[row-1][col+1] == 'S'):
                result += 1

            #EAST Ms
            if (array[row+1][col+1] == 'M' and array[row-1][col+1] == 'M' and 
            array[row+1][col-1] == 'S' and array[row-1][col-1] == 'S'):
                result += 1

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)