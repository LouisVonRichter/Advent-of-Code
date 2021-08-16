from types import prepare_class


with open("day-15.txt") as data:
    inputs = [int(i) for i in data.read().split(",")]


def play(starting_input: list[int], stop_at: int) -> int:
    mem = {}
    for ix, num in enumerate(starting_input):
        mem[num] = (-1, ix + 1)

    ix = len(starting_input)
    latest = starting_input[-1]
    while ix < stop_at:
        ix += 1
        if (latest not in mem) | (mem[latest][0] == -1):
            latest = 0
            mem[latest] = (mem[latest][1], ix)
        else:
            latest = mem[latest][1] - mem[latest][0]
            if latest not in mem:
                mem[latest] = (-1, ix)
            else:
                mem[latest] = (mem[latest][1], ix)
    return latest


def part1(data):
    return play(data, 2020)


def part2(data):
    return play(data, 30000000)


print(part1(inputs))
print(part2(inputs))
