from time import perf_counter

def process_args(args):
    arglist = []
    preamble = 25
    try:
        preamble = int(args[2])
    except Exception:
        pass

    with open(args[1]) as fil:
        for line in fil:
            line = line.strip()
            if line:
                arglist.append(int(line))
    return arglist, preamble

def is_valid(sequence, index, preamble_size):
    if index < preamble_size:
        return True
    value = sequence[index]
    for a in range(index-preamble_size, index):
        for b in range(index-preamble_size, index):
            if a != b and sequence[a]+sequence[b] == value:
                return True
    return False

def part_1(arglist, preamble):
    for index in range(len(arglist)):
        if not is_valid(arglist, index, preamble):
            print(arglist[index])
            break

def get_weakness_subsequence(sequence, weakness):
    running_sum = 0
    partial_sums = []
    for value in sequence:
        running_sum += value
        partial_sums.append(running_sum)
    for a in range(len(partial_sums)):
        for b in range(len(partial_sums)):
            if a != b and partial_sums[b]-partial_sums[a] == weakness:
                return (a+1, b)

def part_2(arglist, preamble):
    weakness = 0
    for index in range(len(arglist)):
        if not is_valid(arglist, index, preamble):
            weakness = arglist[index]
            break
    first, last = get_weakness_subsequence(arglist, weakness)
    subsequence = arglist[first:last+1]
    secret = max(subsequence) + min(subsequence)
    print(secret)

def main(args):
    arglist, preamble = process_args(args)
    print("Part 1")
    p1time = perf_counter()
    part_1(arglist, preamble)
    p1time = perf_counter() - p1time
    print("({} ms)".format(int(p1time*100000)/100))
    print("Part 2")
    p2time = perf_counter()
    part_2(arglist, preamble)
    p2time = perf_counter() - p2time
    print("({} ms)".format(int(p2time*100000)/100))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))