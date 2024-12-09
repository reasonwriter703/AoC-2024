import util
import time
util.set_dir("inputs")
start_time = time.time()
result = 0
file_blocks = []
open_blocks = []

# Read the input file 1 row at a time
for row in open('Day9-input.txt', 'r'):
    for i, char in enumerate(row):
        char = int(char)
        this_block = []
        if i % 2 == 0:  #split input into two lists of lists
            fileID = int(i/2)
            for c in range(char):
                this_block.append(fileID)
            file_blocks.append(this_block)
                
        else:
            for c in range(char):
                this_block.append('.')
            open_blocks.append(this_block)

#for each file block in descending order, look for the leftmost open block in can fit in
for fi, f_block in reversed(list(enumerate(file_blocks))):
    blocklen = '.' * len(file_blocks[fi])
    for oi, o_block in enumerate(open_blocks[0:fi]): #only search to the left of the file block
        if blocklen in ''.join(str(o) for o in o_block):  #if file can fit in block
            for ooi, o_file in enumerate(o_block):
                if o_file == '.':    #move file to first '.' in block
                    open_blocks[oi][ooi:ooi+len(blocklen)] = f_block
                    file_blocks[fi] = ['.' for ffi in file_blocks[fi]]
                    break
            print(fi)
            print(file_blocks[:5])
            print(open_blocks[:5])
            print('')
            break

#zip and flatten remaining file blocks and open blocks
# disk_map = [x for pair in [x for pair in zip(file_blocks, open_blocks) for x in pair] for x in pair]
disk_map = []
for i, o_block in enumerate(open_blocks):
    try:
        disk_map.append(file_blocks[i])
    except IndexError:
        pass
    disk_map.append(o_block)
disk_map = [x for pair in disk_map for x in pair]

for i, n in enumerate(disk_map):
    if n != '.':
        result += i * n

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)