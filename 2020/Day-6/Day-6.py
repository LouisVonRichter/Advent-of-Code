with open("day-6.txt", "r") as data:
    lines = data.readlines()

groups = []
group = []
for question in lines:
    if question != "\n":
        group.append(question.split("\n")[0])
    else:
        groups.append(group)
        group=[]
groups.append(group)

solution_1 = []
for group in groups:
    unique_ques = []
    for ques in group:
        unique_ques.extend([uq for uq in ques])

    solution_1.extend(list(set(unique_ques)))
print(f"Solution 1: {len(solution_1)}")

from collections import Counter

total = 0
for group in groups:
    group_size = len(group)
    counts = Counter("".join(group))

    counts = Counter(list(counts.values()))[group_size]
    total += counts
print(f"Solution 2:", total)