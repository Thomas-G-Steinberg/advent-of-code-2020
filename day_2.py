from time import perf_counter

def process_args(args):
    arglist = []
    with open(args[1]) as fil:
        for line in fil:
            line = line.strip()
            if line:
                sides = line.split(":")
                left = sides[0].split(" ")
                char = left[1].strip()
                nums = left[0].split("-")
                for i in range(len(nums)):
                    nums[i] = int(nums[i])
                passwd = sides[1].strip()
                arglist.append((nums, char, passwd))
    return arglist

def part_1(arglist):
    valid_count = 0
    for entry in arglist:
        if entry[0][0] <= entry[2].count(entry[1]) <= entry[0][1]:
            valid_count += 1
    print(valid_count)

def part_2(arglist):
    valid_count = 0
    for entry in arglist:
        valid = False
        passwd = entry[2]
        ixs = [i-1 for i in entry[0]]
        char = entry[1]
        for ix in ixs:
            if passwd[ix] == char:
                valid = not valid
        if valid:
            valid_count += 1
    print(valid_count)

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