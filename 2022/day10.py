import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def check_signal(cycle):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return cycle * REGISTERS["X"]
    return 0


def do_noop(cycle, *args):
    strength = check_signal(cycle)
    cycle += 1
    return cycle, strength


def do_addx(cycle, *args):
    signal_strength = 0
    for _ in range(2):
        signal_strength += check_signal(cycle)
        cycle += 1
    REGISTERS["X"] += int(args[1])
    return cycle, signal_strength


INSTRUCTIONS = {
    "noop": do_noop,
    "addx": do_addx,
}

REGISTERS = {
    "X": 1
}


def part_one(input_data):
    cycle = 1
    total_strength = 0
    for line in input_data:
        instr = line.split(" ")
        #print(cycle, instr, REGISTERS["X"])
        cycle, strength = INSTRUCTIONS[instr[0]](cycle, *instr)
        total_strength += strength
    return total_strength


def build_instr(input_data):
    instructions = []
    for line in input_data:
        instr = line.split(" ")
        if instr[0] == "noop":
            instructions.append(0)
        else:
            instructions.append(0)
            instructions.append(int(instr[1]))
    return instructions


def part_two(input_data):
    instructions = build_instr(input_data)
    x = 1
    cursor = 0
    for instruction in instructions:
        #print(cursor, x, instruction)
        if cursor == 40:
            cursor = 0
            print()
        if x - 1 <= cursor <= x + 1:
            print("#", end='')
        else:
            print(".", end='')
        cursor += 1
        x += instruction


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day10.txt").read_text().strip().split('\n')
    #DATA = (FILE_DIR / "input" / "day10test.txt").read_text().strip().split('\n')
    print(part_one(DATA))
    part_two(DATA)
