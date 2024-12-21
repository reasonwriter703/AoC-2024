import util
import time
util.set_dir("inputs")
start_time = time.time()
result = 0

row_i = 0
for row in open('Day02-input.txt', 'r'):
    row_i += 1
    report = row.strip().split(' ')
    report = [int(x) for x in report]

    ascending = (report[0] - report[1]) < 0
    for k in range(len(report)):
        try:
            diff = (report[k] - report[k+1])
            if (diff < 0) != ascending or abs(diff) < 1 or abs(diff) > 3:
                print(row_i, 'unsafe')
                break
        except IndexError:
            result += 1
            print(row_i, 'safe')
            break


print('RESULT: ', result)
print('Time taken:', time.time() - start_time)