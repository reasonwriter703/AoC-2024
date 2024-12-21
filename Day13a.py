import util
import time
import numpy as np
util.set_dir("inputs")
start_time = time.time()
result = 0

def get_wins(a, b, prize):
    ax_arr = button_presses(a[0], prize[0])
    bx_arr = button_presses(b[0], prize[0])
    ab_table = ax_arr[:, np.newaxis] + bx_arr   #build a table of all button press sums for X
    ab_table = np.where(ab_table == prize[0])   #keep where X of a+b = X of prize...
    wins = []
    for i, a_presses in enumerate(ab_table[0]):
        b_presses = ab_table[1][i]
        if (a[1] * a_presses) + (b[1] * b_presses) == prize[1]:
            wins.append((a_presses * 3) + b_presses)
    print(wins)
    return min(wins) if len(wins) else 0

def button_presses(button, prize):
    #push button 100 times max, store X coord in list
    list = np.arange(101) * button
    list = list[list <= prize]
    return list

with open('Day13-input.txt', 'r') as file:
    for i, line in enumerate(file):
        match i % 4:
            case 0:
                line = line[10:].strip().split(', ')
                button_a = (int(line[0][2:]), int(line[1][2:]))
            case 1:
                line = line[10:].strip().split(', ')
                button_b = (int(line[0][2:]), int(line[1][2:]))
            case 2:
                line = line[7:].strip().split(', ')
                prize = (int(line[0][2:]), int(line[1][2:]))
            case 3:
                result += get_wins(button_a, button_b, prize)


print('RESULT: ', result)
print('Time taken:', time.time() - start_time)