from time import perf_counter

def process_args(args):
    arglist = []
    with open(args[1]) as fil:
        for line in fil:
            line = line.strip()
            if line:
                arglist.append([line[0],int(line[1:])])
    return arglist

DIRS = {
    'E':(1,0),
    'S':(0,1),
    'W':(-1,0),
    'N':(0,-1),
    0:(1,0),
    1:(0,1),
    2:(-1,0),
    3:(0,-1)
}

def part_1(arglist):
    pos = [0,0]
    facing = 0
    for pair in arglist:
        direction = (0,0)
        char, n = pair
        if char == 'L':
            facing = (facing-(n//90))%4
        elif char == 'R':
            facing = (facing+(n//90))%4
        elif char == 'F':
            direction = DIRS[facing]
        else:
            direction = DIRS[char]
        pos[0] += n*direction[0]
        pos[1] += n*direction[1]
    print(abs(pos[0])+abs(pos[1]))

def part_2(arglist):
    pos = [0,0]
    way_pos = [10,-1]
    for pair in arglist:
        char, n = pair
        if char == 'L' or char == 'R':
            iters = n//90
            if char == 'R':
                iters = (4-iters)%4
            for rep in range(iters):
                tmp = way_pos[1]
                way_pos[1] = -way_pos[0]
                way_pos[0] = tmp
        elif char == 'F':
            pos[0] += n*way_pos[0]
            pos[1] += n*way_pos[1]
        else:
            direction = DIRS[char]
            way_pos[0] += n*direction[0]
            way_pos[1] += n*direction[1]
    print(abs(pos[0])+abs(pos[1]))

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