from time import perf_counter

def process_args(args):
    arglist = []
    group = []
    with open(args[1]) as fil:
        for line in fil:
            line = line.strip()
            if line:
                group.append(line)
            else:
                if len(group)>0:
                    arglist.append(group)
                    group = []
    if len(group)>0:
        arglist.append(group)
    return arglist

def part_1(arglist):
    total = 0
    for group in arglist:
        responses = {}
        for person in group:
            for char in person:
                responses[char]=responses.get(char,0)+1
        total += len(responses)
    print(total)


def part_2(arglist):
    total = 0
    for group in arglist:
        responses = {}
        for person in group:
            for char in person:
                responses[char]=responses.get(char,0)+1
        for key in responses:
            if responses[key] == len(group):
                total += 1
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