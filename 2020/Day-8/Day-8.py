with open("day-8.txt", "r") as data:
    lines = data.readlines()
    lines = [line.rstrip() for line in lines]


def challenge1(lines):
    current_acc = 0
    visited_line = set()
    current_line = 0
    valid_solution = True

    while True:
        if len(lines) - 1 == current_line:
            valid_solution = False

        if current_line in visited_line:
            valid_solution = False
            return current_acc, valid_solution

        inst, acc = lines[current_line].split(" ")
        acc = int(acc)
        visited_line.add(current_line)

        if inst == "nop":
            current_line += 1
        if inst == "acc":
            current_line += acc
            current_line += 1
        if inst == "jmp":
            current_line += acc

        # we got lucky
        if valid_solution == False:
            return current_acc, True


print("Current Accumulator: ", challenge1(lines)[0])
