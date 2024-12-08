import util
import time
util.set_dir("inputs")
start_time = time.time()
result = 0

row_i = 0
def is_safe(rpt):
    for i in range(len(rpt)):
        if i == 0: 
            asc = (rpt[i] < rpt[i+1])
            continue
        diff = rpt[i-1] - rpt[i]
        if abs(diff) < 1 or abs(diff) > 3 or (diff < 0) != asc:
            return False
    return True

for row in open('Day2-input.txt', 'r'):
    row_i += 1
    report = row.strip().split(' ')
    report = [int(x) for x in report]

    if is_safe(report):
        result += 1
        print(row_i, 'safe')
    else:
        #pull one level at a time and recheck
        safe = False
        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)
            if is_safe(new_report):
                result += 1
                print(row_i, 'safe', 'removing lv' + str(i+1))
                safe = True
                break
        if safe == False:
            print(row_i, 'unsafe')

print('RESULT: ', result)
print('Time taken:', time.time() - start_time)