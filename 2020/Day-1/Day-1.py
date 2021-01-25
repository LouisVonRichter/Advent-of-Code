with open('day-1.txt', 'r') as data:
    num = data.readlines()

num = [int(i.split("\n")[0]) for i in num]

print("Question 1\n")
for i in num:
    if 2020-i in num:
        print(i, 2020-i, i*(2020-i))

print("\nQuestion 2\n")
for i in num:
    for j in num:
        if 2020-i - j in num:
            print(2020-i - j, i, j)
            print(1251*289*480)