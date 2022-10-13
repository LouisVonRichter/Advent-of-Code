with open("day-2.txt", "r") as data:
    num = data.readlines()

num = [i.split(" ") for i in num]
forward = 0
depth = 0
for i in num:
    value = int(i[1])
    if i[0] == "forward":
        forward += value
    elif i[0] == "up":
        depth -= value
    elif i[0] == "down":
        depth += value

print("The multiple of depth and forward is: {}".format(forward * depth))

forward = 0
depth = 0
aim = 0

for i in num:
    value = int(i[1])
    if i[0] == "forward":
        forward += value
        interm_depth = value * aim
    elif i[0] == "up":
        aim -= value
    elif i[0] == "down":
        aim += value
    depth += interm_depth
    interm_depth = 0

print("The multiple of depth and forward is: {}".format(forward * depth))
