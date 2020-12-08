def checkPassport(passport, count):
    byr = passport['byr']
    iyr = passport['iyr']
    eyr = passport['eyr']
    hgt = passport['hgt']
    hcl = passport['hcl']
    ecl = passport['ecl']
    pid = passport['pid']
    if len(byr) != 4 or not byr.isdigit() or int(byr) < 1920 or int(byr) > 2002:
        return count
    if len(iyr) != 4 or not iyr.isdigit() or int(iyr) < 2010 or int(iyr) > 2020:
        return count
    if len(eyr) != 4 or not eyr.isdigit() or int(eyr) < 2020 or int(eyr) > 2030:
        return count
    if hgt[-2:] != 'cm' and hgt[-2:] != 'in':
        return count
    if hgt[-2:] == 'cm' and (int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193):
        return count
    if hgt[-2:] == 'in' and (int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76):
        return count
    if hcl[0] != '#':
        return count
    for letter in hcl[1:]:
        if letter not in '0123456789abcdef':
            return count
    if ecl != 'amb' and ecl != 'blu' and ecl != 'brn' and ecl != 'gry' and ecl != 'grn' and ecl != 'hzl' and ecl != 'oth':
        return count
    print(pid)
    if len(pid) != 9 or not pid.isdigit():
        return count

    return count + 1


file = open("input.txt", "r")
input = [str(line).rstrip("\n") for line in file]
input.append("")

count = 0
currPassport = {}
for line in input:
    if line == "":
        if 'byr' in currPassport and 'iyr' in currPassport and  'eyr' in currPassport and  'hgt' in currPassport and  'hcl' in currPassport and  'ecl' in currPassport and  'pid' in currPassport:
            count = checkPassport(currPassport, count)
        currPassport = {}
    else:
        props = line.split(" ")
        for prop in props:
            key,val = prop.split(":")
            currPassport[key] = val
print(count)