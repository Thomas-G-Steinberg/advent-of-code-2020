from time import perf_counter

def process_args(args):
    arglist = []
    with open(args[1]) as fil:
        for line in fil:
            line = line.strip()
            if line:
                arglist.append(line)
    return arglist

def bin_part(inp, highchar):
    size = 1<<len(inp)
    lower = 0
    for char in inp:
        size = size>>1
        if char == highchar:
            lower += size
    return lower

def part_1(arglist):
    high_id = 0
    for seat in arglist:
        row = bin_part(seat[0:7],"B")
        col = bin_part(seat[7:10],"R")
        seat_id = row*8+col
        high_id = max(high_id, seat_id)
    print(high_id)

def part_2(arglist):
    taken = []
    for seat in arglist:
        row = bin_part(seat[0:7],"B")
        col = bin_part(seat[7:10],"R")
        seat_id = row*8+col
        taken.append(seat_id)
    for r in range(128):
        for c in range(8):
            seat_id = r*8+c
            if (seat_id-1) in taken and (seat_id+1) in taken and seat_id not in taken:
                print(seat_id)
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