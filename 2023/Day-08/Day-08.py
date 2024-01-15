import math
from itertools import cycle
import re
from utils import read_multisection_input


def map_transformer(section):
    the_map = {}
    for line in section.split('\n'):
        key, left, right = re.findall(r'[0-9A-Z]{3}', line)
        the_map[key] = (left, right)
    return the_map


instructions, the_map = read_multisection_input(8, [str, map_transformer])


def solve_part_1(instructions, the_map):
    current = 'AAA'
    end = 'ZZZ'

    steps = 0
    for instruction in cycle(instructions):
        steps += 1
        if instruction == 'L':
            current = the_map[current][0]
        if instruction == 'R':
            current = the_map[current][1]
        if current == end:
            return steps
            break


part_1 = solve_part_1(instructions, the_map)
print(f'Solution: {part_1}')


def find_loop(node, the_map, instructions):
    sequence = []
    step = 0
    instructions_length = len(instructions)
    for instruction in cycle(instructions):
        idx = 0 if instruction == 'L' else 1
        node = the_map[node][idx]

        mod_step = step % instructions_length
        if (mod_step, node) in sequence:
            return step, sequence

        sequence.append((mod_step, node))
        step += 1


def find_last_z_node(seq):
    for i in range(len(seq)):
        node = seq[-(i+1)][1]
        if node.endswith('Z'):
            return i


start_nodes = [key for key in the_map if key.endswith('A')]
last_z_in_each_loop = []
for node in start_nodes:
    loop_step, seq = find_loop(node, the_map, instructions)
    last_z_offset = find_last_z_node(seq)
    last_z_in_each_loop.append(loop_step - last_z_offset)

part_2 = math.lcm(*last_z_in_each_loop)
print(f'Solution: {part_2}')
