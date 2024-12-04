import sys
import os
import time
working= os.environ.get("WORKING_DIRECTORY",os.path.dirname(sys.argv[0]) + "/inputs")
if len(sys.argv) > 1: working = sys.argv[1]
os.chdir( working )
start_time = time.time()
result = 0
word = 'XMAS'

def word_search(r, c, x, y, subword):
    global result
    if r < 0 or c < 0:
        return
    if len(subword) == 0:
        # debug_compass = ''
        # if y == 1:
        #     debug_compass = debug_compass + 'S'
        # elif y == -1:
        #     debug_compass = debug_compass + 'N'
        # if x == 1:
        #     debug_compass = debug_compass + 'E'
        # elif x == -1:
        #     debug_compass = debug_compass + 'W'
        # print(r,c,debug_compass)
        result += 1
        return
    try:
        char = array[r+x][c+y]
        if char == subword[0]:
            word_search(r+x, c+y, x, y, subword[1:])
    except IndexError:
        return

# Read the text file and convert it into a 2D array
with open('Day4-input.txt', 'r') as file:
    array = [list(line.strip()) for line in file]

for row, line in enumerate(array):
    for col, char in enumerate(line):
        if array[row][col] == word[0]:
            word_search(row, col, 1, 0, word[1:])
            word_search(row, col, -1, 0, word[1:])
            word_search(row, col, 0, 1, word[1:])
            word_search(row, col, 0, -1, word[1:])
            word_search(row, col, 1, 1, word[1:])
            word_search(row, col, 1, -1, word[1:])
            word_search(row, col, -1, 1, word[1:])
            word_search(row, col, -1, -1, word[1:])

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)