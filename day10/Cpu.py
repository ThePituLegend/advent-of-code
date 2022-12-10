class CPU():
    def __init__(self, dump=False, crt=False):
        self.ram = []
        self.X = 1
        self.pc = 0
        self.clk = 0
        self.signal = 0
        self.dump_enabled = dump
        self.crt_enabled = crt

    def run(self):
        while self.pc < len(self.ram):

            instr = self.ram[self.pc] # Fetch

            self.dump(instr)
            self.draw_pixel()

            self.execute(instr) # (Decode &) Execute

            self.pc += 1
            self.clk += 1

    def execute(self, instr):
        match instr.split():
            case ["addx", val]: # Add to X, 2 cycles
                self.clk += 1 # Noop

                # Next Cycle
                self.dump(instr)
                self.draw_pixel()
                self.X += int(val)

            case ["noop"]: # No operation, 1 cycle
                pass

    def dump(self, instr=None):
        if not self.dump_enabled:
            return

        if (self.clk + 20 + 1) % 40 == 0:
            print(f"--- CLK: {self.clk+1} ---")
            print(f"    PC: {self.pc}")
            print(f"    X: {self.X}")
            print(f"    {instr if instr else 'END OF EXECUTION'} ")
            print(f"--- Signal: {self.clk+1 + self.X} ---")
            print()

            self.signal += (self.clk+1) * self.X

    def draw_pixel(self):
        if not self.crt_enabled:
            return

        if (self.clk % 40) in [self.X-1, self.X, self.X+1]:
            print("#", end="")
        else:
            print(".", end="")

        if (self.clk+1) % 40 == 0:
            print()