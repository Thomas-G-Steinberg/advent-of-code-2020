from time import perf_counter

import numpy as np

def process_args(args):
    arglist = []
    with open(args[1]) as fil:
        for line in fil:
            line = line.strip()
            if line:
                arglist.append(int(line))
    return arglist

def part_1(arglist):
    arglist = sorted(arglist)
    last = arglist[len(arglist)-1]+3
    arglist.append(last)
    prev = 0
    counts = {}
    for i in arglist:
        diff = i-prev
        counts[diff]=counts.get(diff,0)+1
        prev = i
    print(counts[1]*counts[3])


def part_2(arglist):
    arglist.append(0)
    arglist = sorted(arglist)
    last = arglist[len(arglist)-1]+3
    arglist.append(last)
    arglen = len(arglist)

    adj_mat = np.zeros((arglen,arglen), dtype=int)
    for ix in range(arglen):
        current = arglist[ix]
        for ix2 in range(ix,min(ix+4, arglen)):
            if current < arglist[ix2] <= current+3:
                adj_mat[ix][ix2] = 1
    total = 0

    current = adj_mat.copy()
    for i in range(arglen):
        current = np.matmul(current,adj_mat)
        total += current[0][arglen-1]
    print(total)


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