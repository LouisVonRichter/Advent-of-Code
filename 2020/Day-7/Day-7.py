with open("day-7.txt", "r") as data:
    lines = data.readlines()

bag_types = []
all_bags = {}
for line in lines:
    mbag = " ".join(line.split(" ")[:2])
    contains = line[line.index("contain ") + 8 : -1]
    each_contain = contains.split(",")
    each_contain = [cnt.lstrip() for cnt in each_contain]
    each_contain = [" ".join(cont.split(" ")[:-1]) for cont in each_contain]
    each_contain = {
        " ".join(cont.split(" ")[1:]): cont.split(" ")[0] for cont in each_contain
    }
    if mbag not in bag_types:
        bag_types.append(mbag)
    if all_bags.get(mbag):
        each_contain.update(all_bags[mbag])
    all_bags[mbag] = each_contain


def check_bag(bags, my_bag, current_bag):
    if current_bag == my_bag:
        return 1
    if bags.get(current_bag) is None:
        return 0
    else:
        counts = []
        for k, v in bags[current_bag].items():
            counts.append(check_bag(bags, my_bag, k))
        return max(counts)


found_bags = 0
my_bag = "shiny gold"
for k, v in all_bags.items():
    if k != my_bag:
        found_bags += check_bag(all_bags, my_bag, k)
print(f"{found_bags} bags can contain {my_bag} bag.")


test_bags = {
    "shiny gold": {"dark red": 2},
    "dark red": {"dark orange": 2},
    "dark orange": {"dark yellow": 2},
    "dark yellow": {"dark green": 2},
    "dark green": {"dark blue": 2},
    "dark blue": {"dark violet": 2},
    "dark violet": 0,
}

my_bag = "shiny gold"
bags_contains = {}
test_bags = all_bags
for k, v in test_bags.items():
    bags_contains[k] = []
    try:
        for kk, vv in v.items():

            bags_contains[k] += [kk] * int(vv)
    except:
        pass
c = 0


def count_bags(current_bag):
    if current_bag == " " or bags_contains.get(current_bag) is None:
        return 0

    # print("key:", current_bag)
    cnt = len(bags_contains[current_bag])
    cnts = []
    for k in bags_contains[current_bag]:
        cnts.append(count_bags(k))
    return sum(cnts) + cnt


print(f"{my_bag} bag can hold {count_bags('shiny gold')} bags")