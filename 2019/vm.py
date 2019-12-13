class IntProcessor():
    def __init__(self, command, initial_input):
        self.command = command.copy()
        self.command += [0]*1000000
        self.memory = initial_input
        self.memory_ptr = 0
        self.instr_ptr = 0
        self.rel_base = 0

    def read(self, mode, i):
        if mode == 0:
            return self.command[self.command[i]]
        elif mode == 1:
            return self.command[i]
        elif mode == 2:
            return self.command[self.command[i] + self.rel_base]
        else:
            raise NotImplementedError

    def write(self, mode, i, val):
        if mode == 0:
            self.command[self.command[i]] = val
        elif mode == 2:
            self.command[self.command[i] + self.rel_base] = val
        else:
            raise NotImplementedError

    def parse_instruction(self, instruction):
        instruction = "{0:0=5d}".format(instruction)
        p1 = int(instruction[2])
        p2 = int(instruction[1])
        p3 = int(instruction[0])
        opcode = instruction[3:]
        return opcode, p1, p2, p3

    def execute(self):
        while True:
            opcode, p1, p2, p3 = self.parse_instruction(self.command[self.instr_ptr])
            if opcode == "01":
                a = self.read(p1, self.instr_ptr + 1)
                b = self.read(p2, self.instr_ptr + 2)
                self.write(p3, self.instr_ptr + 3, a + b)
                self.instr_ptr += 4

            elif opcode == "02":
                a = self.read(p1, self.instr_ptr + 1)
                b = self.read(p2, self.instr_ptr + 2)
                self.write(p3, self.instr_ptr + 3, a * b)
                self.instr_ptr += 4

            elif opcode == "03":
                if self.memory_ptr < len(self.memory):
                    self.write(p1, self.instr_ptr + 1, self.memory[self.memory_ptr])
                    self.memory_ptr += 1
                else:
                    return -2.5
                self.instr_ptr += 2

            elif opcode == "04":
                output = self.read(p1, self.instr_ptr + 1)
                self.instr_ptr += 2
                return output

            elif opcode == "05":
                test_val = self.read(p1, self.instr_ptr + 1)
                jump_val = self.read(p2, self.instr_ptr + 2)
                if test_val != 0:
                    self.instr_ptr = jump_val
                else:
                    self.instr_ptr += 3

            elif opcode == "06":
                test_val = self.read(p1, self.instr_ptr + 1)
                jump_val = self.read(p2, self.instr_ptr + 2)
                if test_val == 0:
                    self.instr_ptr = jump_val
                else:
                    self.instr_ptr += 3

            elif opcode == "07":
                a = self.read(p1, self.instr_ptr + 1)
                b = self.read(p2, self.instr_ptr + 2)
                if a < b:
                    self.write(p3, self.instr_ptr + 3, 1)
                else:
                    self.write(p3, self.instr_ptr + 3, 0)
                self.instr_ptr += 4

            elif opcode == "08":
                a = self.read(p1, self.instr_ptr + 1)
                b = self.read(p2, self.instr_ptr + 2)
                if a == b:
                    self.write(p3, self.instr_ptr + 3, 1)
                else:
                    self.write(p3, self.instr_ptr + 3, 0)
                self.instr_ptr += 4

            elif opcode == "09":
                val = self.read(p1, self.instr_ptr + 1)
                self.rel_base += val
                self.instr_ptr += 2

            elif opcode == "99":
               return -1.5
