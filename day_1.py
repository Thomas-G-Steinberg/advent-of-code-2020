from time import perf_counter

def process_args(args):
    arglist = []
    with open(args[1]) as fil:
        for line in fil:
            line = line.strip()
            if line:
                arglist.append(int(line))
    return arglist

def part_1(arglist):
    for x in arglist:
        for y in arglist:
            if x+y==2020:
                print(x*y)
                return

def part_2(arglist):
    prod = 1
    for x in arglist:
        for y in arglist:
            for z in arglist:
                if x+y+z==2020:
                    print(x*y*z)
                    return

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