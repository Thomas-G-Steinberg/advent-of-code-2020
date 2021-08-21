from time import perf_counter

import numpy as np

def process_args(args):
    arglist = []
    with open(args[1]) as fil:
        for line in fil:
            line = line.strip()
            if line:
                if ',' in line:
                    arglist.append([int(num) if num.isdigit() else num for num in line.split(",")])
                else:
                    arglist.append(int(line))
    return arglist

def part_1(arglist):
    target = arglist[0]
    busses = arglist[1]
    min_time = None
    bus_id = 0
    wait_time = 0
    for bus in busses:
        if bus != 'x':
            depart = target
            wait = 0
            remain = target%bus
            if remain != 0:
                depart = bus*( (target//bus) + 1)
                wait = depart - target
            if min_time == None or depart < min_time:
                bus_id = bus
                min_time = depart
                wait_time = wait
    print(wait_time*bus_id)

def sort_order(arg):
    return arg[0]

def part_2(arglist):
    busses = arglist[1]
    reduced = [[busses[i],i] for i in range(len(busses)) if busses[i]!='x']
    #reduced[0][1] = reduced[0][0]
    reduced = sorted(reduced, key=sort_order, reverse=True)

    num = np.lcm.reduce([i for i in busses if i != 'x'])
    print(num)
    t = 0
    run = True
    while run:
        run = False
        for entry in reduced:
            if t%entry[0] != entry[0]-entry[1]:
                run = True
                t += num
                break
    print(t)


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