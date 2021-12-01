import numpy as np

inp = np.loadtxt("day-1.txt")

# Part 1
a = np.sum(np.array(np.diff(inp)) > 0, axis=0)
print("The depth has increased {} times".format(a))

# Part 2
b = np.sum(
    np.array(np.diff([sum(inp[i : i + 3]) for i in range(len(inp) - 2)])) > 0, axis=0
)
print("The sliding depth has increased {} times".format(b))
