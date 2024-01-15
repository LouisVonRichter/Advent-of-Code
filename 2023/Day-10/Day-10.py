from itertools import permutations
from utils import read_input

raw_input = read_input(10)


def create_grid(raw_input):
    grid = {}
    start = None
    for y, row in enumerate(raw_input):
        for x, value in enumerate(row):
            if value == 'S':
                start = x + y * -1j
            grid[x + y * -1j] = value
    return grid, start


grid, start = create_grid(raw_input)

OPEN_TO_EAST = set(['-', 'L', 'F', 'S'])
OPEN_TO_WEST = set(['-', 'J', '7', 'S'])
OPEN_TO_NORTH = set(['|', 'J', 'L', 'S'])
OPEN_TO_SOUTH = set(['|', 'F', '7', 'S'])


def are_connected(start, end, grid):
    start_shape = grid[start]
    end_shape = grid[end]
    movement = end - start

    match movement:
        case 1:
            return start_shape in OPEN_TO_EAST and end_shape in OPEN_TO_WEST
        case -1:
            return start_shape in OPEN_TO_WEST and end_shape in OPEN_TO_EAST
        case 1j:
            return start_shape in OPEN_TO_NORTH and end_shape in OPEN_TO_SOUTH
        case -1j:
            return start_shape in OPEN_TO_SOUTH and end_shape in OPEN_TO_NORTH


def get_adjacent(coord):
    return [
        coord + 1,
        coord - 1,
        coord - 1j,
        coord + 1j
    ]


def find_loop(start, grid):
    stack = [start]
    checked = set()

    while stack:
        current = stack.pop()
        if current in checked:
            continue

        checked.add(current)
        neighbors = [
            n
            for n in get_adjacent(current)
            if n in grid and are_connected(current, n, grid)
        ]
        stack.extend(neighbors)

    return checked


loop = find_loop(start, grid)
part_1 = int((len(loop) + 1) / 2)


def is_inside(position, loop, grid):
    """
    Using crossing number algorithm
    to test if we're inside the loop or not
    """
    double_crosses = ['L', '7']
    hits = 0
    northwest = (-1+1j)

    # Move up and left along the diagonal
    position = position + northwest
    # Continue until we go outside the grid
    while position in grid:
        # If we're crossing something in loop, it's a hit
        if position in loop:
            hits += 1
            # If it's a L or 7 curve, count as double cross
            if grid[position] in double_crosses:
                hits += 1
        position = position + northwest

    # If there are an odd number of hits, we're inside
    return hits and hits % 2 != 0


def connect(s, c, grid):
    diff = c - s
    match diff:
        case 1:
            return OPEN_TO_EAST
        case -1:
            return OPEN_TO_WEST
        case 1j:
            return OPEN_TO_NORTH
        case -1j:
            return OPEN_TO_SOUTH


def get_start_pipe(start, loop, grid):
    connections = [pos for pos in get_adjacent(start) if pos in loop]
    for c1, c2 in permutations(connections, 2):
        if are_connected(start, c1, grid) and are_connected(start, c2, grid):
            break

    connection_to_c1 = connect(start, c1, grid)
    connection_to_c2 = connect(start, c2, grid)

    return ((connection_to_c1 & connection_to_c2) - {'S'}).pop()


loop = find_loop(start, grid)
full_grid = grid.copy()
full_grid[start] = get_start_pipe(start, loop, grid)

part_2 = 0
for position in full_grid:
    if not position in loop and is_inside(position, loop, full_grid):
        part_2 += 1


print(f'Solution: {part_1}')
print(f'Solution: {part_2}')
