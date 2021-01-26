with open('day-4.txt', 'r') as data:
    lines = [f.strip() for f in data]

curr_passport = {}
all_passports = []
valid_passports = []
all_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
req_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
key_count = 0

for line in lines:
    if line != "":
        temp_line = line.split(" ")
        temp_dict = {item.split(":")[0]: item.split(":")[1] for item in temp_line}

        for key, value in temp_dict.items():
            curr_passport[key] = value

    else:
        if all(field in curr_passport for field in req_keys):
            valid_passports.append(curr_passport)
        curr_passport = {}
        all_passports.append(curr_passport)
    all_passports.append(curr_passport)

print(len(all_passports), len(valid_passports) + 1)

import re
ecl = "amb blu brn gry grn hzl oth".split(" ")
new_valid_passports = []
for passport in valid_passports:
    valid_keys = 0
    for key, value in passport.items():
        #print(passport)
        if key == "byr":
            if 1920<=int(value)<=2002:
                valid_keys+=1
        elif key == "iyr":
            if 2010<=int(value)<=2020:
                valid_keys+=1
        elif key == "eyr":
            if 2020<=int(value)<=2030:
                valid_keys+=1
        elif key == "hgt":
            if value[-2:] == "cm" and 150<=int(value[:-2])<=193:
                valid_keys+=1
            elif value[-2:] == "in" and 59<=int(value[:-2])<=76:
                valid_keys+=1
        elif key == "hcl":
            if re.match('^#[0-9a-f]{6}$', value):
                valid_keys+=1
        elif key == "ecl" and value in ecl:
            valid_keys+=1
        elif key == "pid":
            if re.match('^[0-9]{9}$', value):
                valid_keys+=1
    if valid_keys==len(all_keys)-1:
        new_valid_passports.append(passport)
    valid_keys=0

print(len(new_valid_passports) + 1)