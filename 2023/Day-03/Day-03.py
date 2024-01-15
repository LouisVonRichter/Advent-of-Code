import math
from collections import namedtuple
from utils import read_input


EMPTY = '.'


def transformer(line):
    return list(line)


def create_engine(schematics):
    engine = {}
    for y, row in enumerate(schematics):
        for x, value in enumerate(row):
            engine[(x, y)] = value
    return engine


schematics = read_input(3, transformer)
engine = create_engine(schematics)


Number = namedtuple('Number', ['value', 'start_position', 'length'])


def find_neighbors(number):
    neighbors = []
    start_x = number.start_position[0]
    y = number.start_position[1]
    for x in range(start_x, start_x + number.length):
        neighbors.extend([
            (x-1, y-1),
            (x, y-1),
            (x+1, y-1),
            (x-1, y),
            (x+1, y),
            (x-1, y+1),
            (x, y+1),
            (x+1, y+1)
        ])
    return neighbors


def is_symbol(character):
    return character != EMPTY and not character.isdigit()


def is_valid_part_number(number, engine):
    for neighbor in find_neighbors(number):
        if is_symbol(engine.get(neighbor, EMPTY)):
            return True
    return False


def sort_by_rows_then_columns(x): return (x[0][1], x[0][0])


def find_numbers(engine):
    numbers = []

    reading_number = ''
    start_position = None
    for pos, value in sorted(engine.items(), key=sort_by_rows_then_columns):
        if value.isdigit():
            # We are currently in the middle of a number
            if reading_number:
                # If we wrap to new line, we need to stop old number and start new
                if pos[0] == 0:
                    numbers.append(
                        Number(
                            value=int(reading_number),
                            start_position=start_position,
                            length=len(reading_number)
                        )
                    )
                    reading_number = value
                    start_position = pos
                else:
                    reading_number += value
            # We start to read a number
            if not reading_number:
                start_position = pos
                reading_number = value
        # We finished reading a number
        elif reading_number:
            numbers.append(
                Number(
                    value=int(reading_number),
                    start_position=start_position,
                    length=len(reading_number)
                )
            )
            reading_number = ""
            start_pos = None
    return numbers


def calculate_sum(engine):
    numbers = find_numbers(engine)

    valid_numbers = []
    for number in numbers:
        if is_valid_part_number(number, engine):
            valid_numbers.append(number)

    return sum(n.value for n in valid_numbers)


part_1 = calculate_sum(engine)
print(f'Solution: {part_1}')


GEAR = '*'


def find_neighboring_numbers(gear_position, numbers):
    connected = []
    for number in numbers:
        number_neighbors = find_neighbors(number)
        if gear_position in number_neighbors:
            connected.append(number)
    return connected


def calculate_gear_ratio_sum(engine):
    gear_ratios = []
    numbers = find_numbers(engine)
    for position, value in engine.items():
        if value != GEAR:
            continue
        connected_numbers = find_neighboring_numbers(position, numbers)
        if len(connected_numbers) == 2:
            gear_ratios.append(math.prod((n.value for n in connected_numbers)))
    return sum(gear_ratios)


part_2 = calculate_gear_ratio_sum(engine)
print(f'Solution: {part_2}')
