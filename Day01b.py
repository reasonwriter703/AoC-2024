import util
import time
util.set_dir("inputs")
start_time = time.time()
result = 0

list_x = []
list_y = []
for row in open('Day01-input.txt', 'r'):
    x, y = row.strip().split('   ')
    list_x.append(int(x))
    list_y.append(int(y))

for id_x in list_x:
    count = 0
    for id_y in list_y:
        if id_x == id_y:
            count += 1
    result += (id_x * count)

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)