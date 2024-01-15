import re
from collections import namedtuple

Range = namedtuple('Range', ['dest_start', 'source_start', 'range'])

input = './Day-05.txt'

with open(input) as raw_input:
    data_sections = raw_input.read().split('\n\n')

seeds = [int(seed) for seed in re.findall(
    r'\d+', data_sections[0].split(': ')[1])]


def process_ranges(section):
    lines = section.split('\n')[1:]
    ranges = []
    for line in lines:
        numbers = [int(value) for value in re.findall(r'\d+', line)]
        ranges.append(Range(*numbers))
    return ranges


seed_to_soil = process_ranges(data_sections[1])
soil_to_fertilizer = process_ranges(data_sections[2])
fertilizer_to_water = process_ranges(data_sections[3])
water_to_light = process_ranges(data_sections[4])
light_to_temperature = process_ranges(data_sections[5])
temperature_to_humidity = process_ranges(data_sections[6])
humidity_to_location = process_ranges(data_sections[7])

ranges = [
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location
]


def map_to_value(source, r):
    if source >= r.source_start and source <= r.source_start + r.range:
        n = source - r.source_start
        return r.dest_start + n
    else:
        return -1


def calculate_location(seed, ranges):
    source = seed
    for _range in ranges:
        for individual_range in _range:
            potential = map_to_value(source, individual_range)
            if potential != -1:
                source = potential
                break
            else:
                continue
    return source


smallest = None
for seed in seeds:
    location = calculate_location(seed, ranges)
    if not smallest or location < smallest:
        smallest = location

print(f'Solution: {smallest}')


def map_to_prev(dest, r):
    low = r.dest_start
    high = r.dest_start + r.range - 1
    # Any source numbers that aren't mapped
    # correspond to the same destination number.
    if dest < low or dest > high:
        return -1
    else:
        return dest - r.dest_start + r.source_start


def find_seed(location, ranges):
    src = location
    for _range in ranges:
        for individual_range in _range:
            potential = map_to_prev(src, individual_range)
            if potential != -1:
                src = potential
                break
    return src


def get_all_seed_ranges(data_sections):
    seed_range_input = [int(seed) for seed in re.findall(
        r'\d+', data_sections[0].split(': ')[1])]
    return zip(seed_range_input[::2], seed_range_input[1::2])


def is_valid_seed(seed, seed_ranges):
    for seed_range in seed_ranges:
        if seed_range[0] < seed < seed_range[0] + seed_range[1]:
            return True
    return False


location_ranges = ranges[-1]

highest_location_range = max(
    location_ranges, key=lambda range: range.dest_start)
max_location = highest_location_range.dest_start + highest_location_range.range
all_locations = range(1, max_location)

seed_ranges = list(get_all_seed_ranges(data_sections))

part_2 = None

for location in all_locations:
    seed = find_seed(location, ranges[-1::-1])
    if is_valid_seed(seed, seed_ranges):
        print(f'Found {seed=} at {location=}')
        part_2 = location
        break
print(f'Solution: {part_2}')
