from utils import read_multisection_input


def transformer(section):
    return section.split('\n')


grids = read_multisection_input(13, [transformer])


def is_mirror_line(grid, line):
    up = line-1
    down = line

    while up >= 0 and down < len(grid):
        if grid[up] != grid[down]:
            return False
        up -= 1
        down += 1
    return True


def find_reflection_point(grid):
    for y in range(1, len(grid)):
        if is_mirror_line(grid, y):
            return 100 * y

    transposed = list(zip(*grid))
    for x in range(1, len(transposed)):
        if is_mirror_line(transposed, x):
            return x

    return None


part_1 = 0
reflection_points = {}
for i, grid in enumerate(grids):
    reflection_point = find_reflection_point(grid)
    reflection_points[i] = reflection_point
    part_1 += reflection_point

print(f'Solution: {part_1}')
