import re
from utils import read_input

calibrations = read_input(1)


def recalibrate(calibrations):
    result = 0
    for calibration in calibrations:
        numbers = re.findall(r'\d', calibration)
        calibration_value = int(f'{numbers[0]}{numbers[-1]}')
        result += calibration_value
    return result


part_1 = recalibrate(calibrations)
print(f'Solution: {part_1}')


def convert_to_int(numberish):
    names_to_values = [
        'zero', 'one', 'two',
        'three', 'four', 'five',
        'six', 'seven', 'eight',
        'nine'
    ]
    try:
        return int(numberish)
    except ValueError:
        return names_to_values.index(numberish)


def calibrate_p2(calibrations):
    result = 0
    for calibration in calibrations:
        numbers = re.findall(
            r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', calibration)
        first, last = convert_to_int(numbers[0]), convert_to_int(numbers[-1])
        calibration_value = int(f'{first}{last}')
        result += calibration_value
    return result


part_2 = calibrate_p2(calibrations)
print(f'Solution: {part_2}')
