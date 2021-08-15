from collections import Counter

with open('day-10.txt') as data:
    inputs = [
        int(line)
        for line in data.read().splitlines()
    ]

jolts = sorted(inputs)
jolts.append(jolts[-1] + 3)

def part1(nums):
    last_jolt = 0
    diffs = [0, 0, 0, 0]

    for jolt in jolts:
        diffs[jolt - last_jolt] += 1
        last_jolt = jolt
 
    return diffs[1] * diffs[3]

def part2(nums):
    dp = Counter()
    dp[0] = 1

    for jolt in jolts:
        dp[jolt] = dp[jolt - 1] + dp[jolt - 2] + dp[jolt - 3]

    return dp[jolts[-1]]

print(part1(inputs))
print(part2(inputs))