from time import perf_counter

def process_args(args):
    arglist = []
    entry = {}
    with open(args[1]) as fil:
        for line in fil:
            line = line.strip()
            if line:
                pairs = line.strip().split(" ")
                for pair in pairs:
                    kv = pair.split(":")
                    entry[kv[0]]=kv[1]
            else:
                if len(entry) > 0:
                    arglist.append(entry)
                    entry = {}
    if len(entry) > 0:
        arglist.append(entry)
        entry = {}
    return arglist

def part_1(arglist):
    valid = 0
    required_fields = (
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid" # ,"cid" exclude country id
    )
    for passport in arglist:
        if all(field in passport for field in required_fields):
            valid += 1
    print(valid)

def validate_byr(val):
    return val.isdigit() and (1920 <= int(val) <= 2002)

def validate_iyr(val):
    return val.isdigit() and (2010 <= int(val) <= 2020)

def validate_eyr(val):
    return val.isdigit() and (2020 <= int(val) <= 2030)

def validate_hgt(val):
    if val.endswith("cm"):
        val = val[0:-2]
        if val.isdigit():
            return 150<=int(val)<=193
        else:
            return False
    elif val.endswith("in"):
        val = val[0:-2]
        if val.isdigit():
            return 59<=int(val)<=76
        else:
            return False
    return False

def validate_hcl(val):
    if len(val)==7 and val[0]=='#':
        for chr in val[1:]:
            if chr not in "abcdef1234567890":
                return False
        return True
    return False

def validate_ecl(val):
    return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate_pid(val):
    return val.isdigit() and len(val) == 9

def part_2(arglist):
    valid = 0
    validators = {
        "byr":validate_byr,
        "iyr":validate_iyr,
        "eyr":validate_eyr,
        "hgt":validate_hgt,
        "hcl":validate_hcl,
        "ecl":validate_ecl,
        "pid":validate_pid
    }
    for passport in arglist:
        if all( (field in passport and validators[field](passport[field])) for field in validators):
            valid += 1
    print(valid)

def main(args):
    arglist = process_args(args)
    print("Part 1")
    p1time = perf_counter()
    part_1(arglist)
    p1time = perf_counter() - p1time
    print("({} ms)".format(int(p1time*100000)/100))
    print("Part 2")
    p2time = perf_counter()
    part_2(arglist)
    p2time = perf_counter() - p2time
    print("({} ms)".format(int(p2time*100000)/100))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))