import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def run(instructions):
    acc = 0
    i = 0
    while True:
        command, num, used = instructions[i]
        instructions[i] = (command, num, True)
        # print(f"Command: {command} {num}")
        if used:
            return acc, False
        if command == "acc":
            acc += num
            i += 1
        elif command == "jmp":
            i += num
        else:
            i += 1

        if i == len(instructions):
            return acc, True

def part_two(instructions):
    for i in range(len(instructions)):
        command, num, used = instructions[i]
        if command == "acc":
            continue
        mutated_instructions = instructions.copy()
        if command == "nop":
            mutated_instructions[i] = ("jmp", num, used)
        else:
            mutated_instructions[i] = ("nop", num, used)
        acc, success = run(mutated_instructions)
        if success:
            return acc


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day8.txt").read_text().strip().split('\n')
    instructions = {}
    for i, line in enumerate(DATA):
        command, num = line.split(' ')
        if num[0] == "+":
            num = int(num[1:])
        else:
            num = int(num)
        instructions[i] = (command, num, False)

    print(run(instructions.copy()))
    print(part_two(instructions.copy()))
