from functools import cache
from itertools import product
from utils import read_input


def transformer(line):
    springs, notes = line.split(' ')
    notes = [int(v) for v in notes.split(',')]
    return springs, tuple(notes)


hot_springs = read_input(12, transformer)


class Spring:
    OPERATIONAL = '.'
    DAMAGED = '#'
    UNKNOWN = '?'


def is_valid_order(springs, damaged):
    damaged_springs = [len(s) for s in springs.split(Spring.OPERATIONAL) if s]
    return damaged_springs == list(damaged)


def find_valid_ones(springs, notes):
    valid_ones = 0
    unknowns = springs.count(Spring.UNKNOWN)
    options = product(Spring.OPERATIONAL + Spring.DAMAGED, repeat=unknowns)
    for opt in options:
        new_springs = springs
        for char in opt:
            new_springs = new_springs.replace(Spring.UNKNOWN, char, 1)
        if is_valid_order(new_springs, notes):
            valid_ones += 1
    return valid_ones


part_1 = 0
for springs, notes in hot_springs:
    part_1 += find_valid_ones(springs, notes)

print(f'Solution: {part_1}')


@cache
def how_many_valid_arraignments(springs, notes, count=0):
    # All springs accounted for
    if not springs and count > 0:  # Last spring was damaged
        if len(notes) == 1 and count == notes[0]:
            return 1
        else:
            return 0
    if not springs and count == 0:  # Last spring was operational
        if len(notes) == 0:
            return 1
        else:
            return 0

    # We saw more damaged springs in a row than there
    # should be according to the notes so it is not valid
    if count > 0 and (not notes or count > notes[0]):
        return 0

    # So far everything's good but we have more springs to see
    first, rest = springs[0], springs[1:]
    match first:
        case Spring.OPERATIONAL:
            if count > 0:  # We finished a run of damaged springs
                if count != notes[0]:
                    return 0
                else:  # Last spring was also operational
                    notes = notes[1:]
            return how_many_valid_arraignments(rest, notes, 0)
        case Spring.DAMAGED:
            # Increase damage count
            return how_many_valid_arraignments(rest, notes, count + 1)
        case Spring.UNKNOWN:
            # We finished a run of damaged springs
            if not notes or count == notes[0]:
                return how_many_valid_arraignments(rest, notes[1:], 0)
            else:
                if count > 0:
                    # We are in the middle of a run of damaged springs
                    return how_many_valid_arraignments(rest, notes, count + 1)
                else:
                    # This unknown could be a . or # so let's count both options
                    return (how_many_valid_arraignments(rest, notes, count + 1) +
                            how_many_valid_arraignments(rest, notes, count))
        case _:
            raise ValueError(f'{first} is an invalid spring')


part_2 = 0
for springs, notes in hot_springs:
    springs = '?'.join([springs] * 5)
    notes = notes * 5
    part_2 += how_many_valid_arraignments(springs, notes)

print(f'Solution: {part_2}')
