with open("day-2.txt", "r") as data:
    passw = data.readlines()

passw = [i.split("\n")[0] for i in passw]

valid_2 = []
valid_1 = []
for line in passw:
    key, value = line.split(": ")
    char = key.split(" ")[1]

    n1, n2 = key.split(" ")[0].split("-")
    n1, n2 = int(n1) - 1, int(n2) - 1

    if n1 + 1 <= value.count(char) <= n2 + 1:
        valid_1.append(line)

    c = 0
    try:

        if value[int(n1)] == char:
            c += 1
        if value[int(n2)] == char:
            c += 1
        if c == 1:
            valid_2.append(line)
    except:
        pass
print(f" Solution 1: {len(valid_1)}\nSolution 2:{len(valid_2)}")