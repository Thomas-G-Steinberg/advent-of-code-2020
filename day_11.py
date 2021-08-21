from time import perf_counter

def process_args(args):
    arglist = []
    with open(args[1]) as fil:
        for line in fil:
            line = line.strip()
            if line:
                arglist.append(list(line))
    return arglist

def print_grid(grid):
    print()
    for row in grid:
        print(''.join(row))

def iterate(current, next_iter, height, width):
    changed = 0
    for y in range(height):
        for x in range(width):
            char = current[y][x]
            if char == '.':
                next_iter[y][x] = '.'
            else:
                adjacent = 0
                for my in range(max(0, y-1),min(height,y+2)):
                    for mx in range(max(0, x-1),min(width,x+2)):
                        if mx != x or my != y:
                            if current[my][mx] == '#':
                                adjacent += 1
                if char == 'L' and adjacent == 0:
                    next_iter[y][x] = '#'
                    changed += 1
                elif char == '#' and adjacent >= 4:
                    next_iter[y][x] = 'L'
                    changed += 1
                else:
                    next_iter[y][x] = char
    return changed

DIR_LIST = (
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,-1),
    (0,1),
    (1,-1),
    (1,0),
    (1,1)
)

def build_lookup(current, lookup, height, width):
    for row in range(height):
        row_lookups = []
        for col in range(width):
            coords = []
            for d in DIR_LIST:
                x, y = col+d[0], row+d[1]
                while (0<=x<width) and (0<=y<height):
                    if current[y][x] != '.':
                        coords.append((x,y))
                        break
                    x += d[0]
                    y += d[1]
            row_lookups.append(coords)
        lookup.append(row_lookups)


def iterate_modified(current, next_iter, height, width, lookup):
    if len(lookup) == 0:
        build_lookup(current, lookup, height, width)
    changed = 0
    for y in range(height):
        for x in range(width):
            char = current[y][x]
            if char == '.':
                next_iter[y][x] = '.'
            else:
                adjacent = 0
                for coord in lookup[y][x]:
                    mx, my = coord
                    if current[my][mx] == '#':
                        adjacent += 1
                if char == 'L' and adjacent == 0:
                    next_iter[y][x] = '#'
                    changed += 1
                elif char == '#' and adjacent >= 5:
                    next_iter[y][x] = 'L'
                    changed += 1
                else:
                    next_iter[y][x] = char
    return changed

def part_1(arglist):
    grid_h = len(arglist)
    grid_w = len(arglist[0])
    current = [[arglist[y][x] for x in range(grid_w)] for y in range(grid_h)]
    next_iter = [['.' for x in range(grid_w)] for y in range(grid_h)]
    while True:
        changed = iterate(current, next_iter, grid_h, grid_w)
        tmp = current
        current = next_iter
        next_iter = tmp
        if changed == 0:
            break
    occupied = 0
    for row in current:
        occupied += row.count('#')
    print(occupied)


def part_2(arglist):
    grid_h = len(arglist)
    grid_w = len(arglist[0])
    current = [[arglist[y][x] for x in range(grid_w)] for y in range(grid_h)]
    next_iter = [['.' for x in range(grid_w)] for y in range(grid_h)]
    lookup = []
    while True:
        changed = iterate_modified(current, next_iter, grid_h, grid_w, lookup)
        tmp = current
        current = next_iter
        next_iter = tmp
        if changed == 0:
            break
    occupied = 0
    for row in current:
        occupied += row.count('#')
    print(occupied)

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