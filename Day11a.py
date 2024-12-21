import util
import time
import numpy as np
from functools import cache
util.set_dir("inputs")
start_time = time.time()
result = 0

@cache
def blink(stone, blinks):
    if blinks == 0:
        return stone
    if stone == 0:
        return blink(1, blinks - 1)
    digits = len(str(stone))
    if digits % 2 == 0:
        return blink(split_stone(digits, stone), blinks - 1)
    else:
        return blink(stone * 2024, blinks - 1)

@cache
def split_stone(digits, stone):
    stone = [int(str(stone)[:int(digits/2)]), int(str(stone)[-int(digits/2):])]
    return [s for xs in stone for s in xs]

# Read the input file 1 row at a time
for row in open('Day11-input.txt', 'r'):
    stones = [int(n) for n in row.split()]

    stones = [blink(stone, 25) for stone in stones]

print('RESULT: ', len(stones))
print('Time taken:', time.time() - start_time)