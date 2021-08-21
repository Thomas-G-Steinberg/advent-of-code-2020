from time import perf_counter

def process_args(args):
    arglist = []
    with open(args[1]) as fil:
        for line in fil:
            line = line.strip()
            if line:
                arglist.append(line)
    return arglist

def count_trees(arglist, slope):
    period = len(arglist[0])
    run = len(arglist)
    position = [0, 0]
    trees = 0
    while position[1] < run:
        current = arglist[position[1]][position[0]]
        if current == '#':
            trees += 1
        position[0] = (position[0]+slope[0])%period
        position[1] += slope[1]
    return trees

def part_1(arglist):
    print(count_trees(arglist,[3,1]))

def part_2(arglist):
    prod = 1
    slopes = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2]
    ]
    for slope in slopes:
        prod = prod * count_trees(arglist, slope)
    print(prod)

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