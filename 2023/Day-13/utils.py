import os
import sys


def read_input(day, transformer=str, example=False):
    try:
        if example:
            filename = f'Day-{day}.txt'
        else:
            filename = f'Day-{day}.txt'
        with open(os.path.join('.', filename)) as input_file:
            return [transformer(line.strip()) for line in input_file]
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)


def read_multisection_input(day, transformers=None, example=False):
    """
    Read multisection puzzle input for file `/inputs/day_{day}.txt'
    and apply transformer function to each section.

    If `example` is set to True, read file `/inputs/day_{day}_example.txt`
    instead
    """

    try:
        if example:
            filename = f'Day-{day}.txt'
        else:
            filename = f'Day-{day}.txt'
        with open(os.path.join('.', filename)) as input_file:
            sections = input_file.read().split('\n\n')
            return [transformer(section) for section, transformer in zip(sections, transformers)]
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
