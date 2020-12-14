import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent

def parse_line(line):
    op, val = line.split(' = ')
    if op == 'mask':
        return 'mask', None, val
    else:
        addr = int(op[op.index("[") + 1:op.index("]")])
        val = int(val)
        return "mem", addr, val

def apply_mask_one(mask, val):
    bin_val = ["0"]*36
    for i, c in enumerate([num for num in format(val, "b")][::-1]):
        bin_val[35 - i] = c
    for i, c in enumerate(mask):
        if c == "X":
            continue
        else:
            bin_val[i] = c
    return int(''.join(bin_val), 2)

def apply_mask_two(mask, val):
    addr_vals = []
    bin_val = ["0"]*36
    for i, c in enumerate([num for num in format(val, "b")][::-1]):
        bin_val[35 - i] = c
    for i, c in enumerate(mask):
        if c == "X":
            bin_val[i] = "X"
        elif c == "0":
            continue
        else:
            bin_val[i] = "1"
    for i, c in enumerate(bin_val):
        if c != "X":
            if not addr_vals:
                continue
            else:
                for addr in addr_vals:
                    addr.append(c)
        else:
            if not addr_vals:
                zero_list = list(bin_val[:i])
                zero_list.append("0")
                one_list = list(bin_val[:i])
                one_list.append("1")
                addr_vals.append(zero_list)
                addr_vals.append(one_list)
            else:
                new_addr_vals = []
                for addr in addr_vals:
                    zero_list = list(addr)
                    zero_list.append("0")
                    one_list = list(addr)
                    one_list.append("1")
                    new_addr_vals.append(zero_list)
                    new_addr_vals.append(one_list)
                addr_vals = new_addr_vals
    if not addr_vals:
        return [int(''.join(bin_val), 2)]
    else:
        return [int(''.join(addr), 2) for addr in addr_vals]

def part_one(input_data):
    current_mask = None
    memory = {}
    for line in input_data:
       op, addr, val = parse_line(line)
       if op == "mask":
           current_mask = val
       else:
          memory[addr] = apply_mask_one(current_mask, val)
    return sum([value for value in memory.values()])

def part_two(input_data):
    current_mask = None
    memory = {}
    for line in input_data:
       op, addr, val = parse_line(line)
       if op == "mask":
           current_mask = val
       else:
          addr_vals = apply_mask_two(current_mask, addr)
          for addr_val in addr_vals:
              memory[addr_val] = val
    return sum([value for value in memory.values()])

if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day14.txt").read_text().strip().split('\n')
    print(part_one(DATA))
    print(part_two(DATA))
