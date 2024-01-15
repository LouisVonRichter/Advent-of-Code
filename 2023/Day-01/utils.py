import os
import sys


def read_input(day, transformer=str, example=False):
    try:
        if example:
            filename = f'day-0{day}_example.txt'
        else:
            filename = f'Day-0{day}.txt'
        with open(os.path.join('.', filename)) as input_file:
            return [transformer(line.strip()) for line in input_file]
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
