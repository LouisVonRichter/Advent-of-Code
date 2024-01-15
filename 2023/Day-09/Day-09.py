from collections import deque
from utils import read_input
from itertools import tee


def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def transformer(line):
    return [int(value) for value in line.split(' ')]


sequences = read_input(9, transformer)


def create_diff_sequences(sequence):
    full_sequence = [sequence[:]]
    while True:
        current_differences = [
            current - previous
            for previous, current
            in zip(sequence, sequence[1:])
        ]

        full_sequence.append(current_differences)

        sequence = current_differences
        if all(difference == 0 for difference in current_differences):
            break

    return full_sequence


def calculate_next_number(sequence):
    differences = create_diff_sequences(sequence)
    differences = differences[::-1]
    for current, previous in pairwise(differences):
        previous.append(current[-1] + previous[-1])

    return differences[-1][-1]


part_1 = 0
for seq in sequences:
    part_1 += calculate_next_number(seq)

print(f'Solution: {part_1}')


def calculate_prev_number(sequence):
    differences = [
        deque(seq)
        for seq
        in create_diff_sequences(sequence)[::-1]
    ]

    for current, previous in pairwise(differences):
        previous.appendleft(previous[0] - current[0])

    return differences[-1][0]


part_2 = 0
for seq in sequences:
    prev = calculate_prev_number(seq)
    part_2 += prev

print(f'Solution: {part_2}')
