from time import perf_counter

def process_args(args):
    arglist = {}
    with open(args[1]) as fil:
        for line in fil:
            line = line.strip()
            lrsplit = line.split("contain")
            lhs = lrsplit[0].strip()[0:-5].strip()
            rhs = lrsplit[1].strip(" .").split(",")
            for ix in range(len(rhs)):
                res = rhs[ix]
                tokenized = res.strip().split(" ")
                if tokenized[0] == "no":
                    rhs = []
                    break
                count = int(tokenized[0])
                name = " ".join(tokenized[1:-1])
                rhs[ix] = [count, name]
            if line:
                arglist[lhs]=rhs
    return arglist

def part_1(arglist):
    target = "shiny gold"
    back = {}
    for key in arglist:
        for res in arglist[key]:
            count, name = res
            entry = back.get(name, set())
            if key not in entry:
                entry.add(key)
            back[name] = entry

    total = 0

    visited = set()
    next_iter = set(back[target])
    while len(next_iter) > 0:
        traverse = set()
        for bag in next_iter:
            if bag not in visited:
                total += 1
                visited.add(bag)
                if bag in back:
                    traverse.update(back[bag])
        next_iter = traverse
    print(total)

def get_bags_in_bag(target, arglist, solved={}):
    entry = arglist[target]
    total = 0
    for bag in entry:
        count, name = bag
        total += count
        if name in solved:
            total += count * solved[name]
        else:
            solution = get_bags_in_bag(name, arglist, solved)
            solved[name] = solution
            total += count * solution
    return total

def part_2(arglist):
    print(get_bags_in_bag("shiny gold", arglist))

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