import math

with open("day-1.txt") as data:
    inputs = [int(i) for i in data.read().splitlines()]


def part1(weights):
    tot = 0
    for weight in weights:
        tot += math.floor(weight / 3) - 2

    return tot


def part2(fuels):
    sum = 0
    for fuel in fuels:
        f = fuel / 3 - 2
        while f > 0:
            sum += f
            f = f / 3 - 2
    return sum


print(part1(inputs))
print(part2(inputs))
