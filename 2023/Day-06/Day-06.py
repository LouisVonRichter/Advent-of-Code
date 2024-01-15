from utils import read_input
import re


def transformer(line):
    return [int(v) for v in re.findall(r'\d+', line)]


times, records = read_input(6, transformer)


def find_winning_strategies(time, record):
    low_winner = 0
    high_winner = 0
    for pressed_down in range(0, time+1):
        travelled = (time - pressed_down) * pressed_down
        if travelled > record:
            low_winner = pressed_down
            break
    for pressed_down in range(time, 0, -1):
        travelled = (time - pressed_down) * pressed_down
        if travelled > record:
            high_winner = time - pressed_down
            break
    # We add +1 here because for a time of 7 ms, there are 8 attempts (one at 0ms)
    return (time + 1) - low_winner - high_winner


part_1 = 1
for time, record in zip(times, records):
    part_1 *= find_winning_strategies(time, record)
print(f'Solution: {part_1}')

new_time = int(''.join(str(t) for t in times))
new_record = int(''.join(str(d) for d in records))

part_2 = find_winning_strategies(new_time, new_record)
print(f'Solution: {part_2}')
