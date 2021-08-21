from time import perf_counter

def process_args(args):
    arglist = []
    with open(args[1]) as fil:
        for line in fil:
            line = line.strip()
            if line:
                arglist.append(line.split())
    return arglist

class CodeMachine:
    def __init__(self, program):
        self.orig_program = [i for i in program]
        self.program = [i for i in program]
        self.visited = [False for i in program]
        self.pc = 0
        self.acc = 0
        self.halt = False
        self.success = False
    
    def single_step(self):
        instr, offset = self.program[self.pc]
        offset = int(offset)
        if not self.visited[self.pc]:
            self.visited[self.pc] = True
        else:
            self.halt = True
            return

        if instr == "acc":
            self.acc += offset
            self.pc += 1
        elif instr == "jmp":
            self.pc += offset
        elif instr == "nop":
            self.pc += 1

        if self.pc == len(self.program):
            self.halt = True
            self.success = True
    
    def run(self):
        while not self.halt:
            self.single_step()

    def get_corruption_candidates(self):
        ixs = []
        for ix in range(len(self.program)):
            if self.program[ix][0] != "acc":
                ixs.append(ix)
        return ixs

    def reset_and_toggle(self, ix):
        self.program = [[i for i in line] for line in self.orig_program]
        self.visited = [False for i in self.orig_program]
        self.pc = 0
        self.acc = 0
        self.halt = False
        self.success = False
        if self.program[ix][0] == "jmp":
            self.program[ix][0] = "nop"
        elif self.program[ix][0] == "nop":
            self.program[ix][0] = "jmp"

def part_1(arglist):
    mach = CodeMachine(arglist)
    mach.run()
    print(mach.acc)

def part_2(arglist):
    mach = CodeMachine(arglist)
    ixs = mach.get_corruption_candidates()
    for ix in ixs:
        mach.reset_and_toggle(ix)
        mach.run()
        if mach.success:
            print(mach.acc)
            break


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