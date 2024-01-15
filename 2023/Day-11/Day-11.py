from itertools import combinations
from utils import read_input

GALAXY = '#'

raw_space = read_input(11)

space = {}
for y, row in enumerate(raw_space):
    for x, cell in enumerate(row):
        if cell == GALAXY:
            space[x + y * -1j] = GALAXY


def expand_space(space):
    min_y = int(min(coord.imag for coord in space))
    max_x = int(max(coord.real for coord in space))

    should_expand_rows = []
    for y in range(0, min_y, -1):
        has_galaxies = any(cell for cell in space if int(cell.imag) == y)
        if not has_galaxies:
            should_expand_rows.append(y)

    should_expand_columns = []
    for x in range(max_x):
        has_galaxies = any(cell for cell in space if int(cell.real) == x)
        if not has_galaxies:
            should_expand_columns.append(x)

    new_space = {}
    for galaxy in space:
        shift_right = len(
            [column for column in should_expand_columns if galaxy.real > column])
        shift_down = len(
            [row for row in should_expand_rows if galaxy.imag < row])
        new_space[galaxy + (shift_right + shift_down * -1j)] = GALAXY

    return new_space


def calculate_distance(one, another):
    return int(abs(one.real - another.real) + abs(one.imag - another.imag))


new_space = expand_space(space)

part_1 = 0
for one, another in combinations(new_space, 2):
    distance = calculate_distance(one, another)
    part_1 += distance

print(f'Solution: {part_1}')


def expand_space_more(space, multiplier):
    min_y = int(min(coord.imag for coord in space))
    max_x = int(max(coord.real for coord in space))

    should_expand_rows = []
    for y in range(0, min_y, -1):
        has_galaxies = any(cell for cell in space if int(cell.imag) == y)
        if not has_galaxies:
            should_expand_rows.append(y)

    should_expand_columns = []
    for x in range(max_x):
        has_galaxies = any(cell for cell in space if int(cell.real) == x)
        if not has_galaxies:
            should_expand_columns.append(x)

    new_space = {}
    for galaxy in space:
        shift_right = len(
            [column for column in should_expand_columns if galaxy.real > column]) * (multiplier - 1)
        shift_down = len(
            [row for row in should_expand_rows if galaxy.imag < row]) * (multiplier - 1)
        new_space[galaxy + (shift_right + shift_down * -1j)] = GALAXY

    return new_space


bigger_space = expand_space_more(space, 1_000_000)

part_2 = 0
for one, another in combinations(bigger_space, 2):
    distance = calculate_distance(one, another)
    part_2 += distance

print(f'Solution: {part_2}')
