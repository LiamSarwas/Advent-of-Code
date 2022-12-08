import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent

priority = {}
for x in range(97, 123):
    priority[chr(x)] = x - 96
for x in range(65, 91):
    priority[chr(x)] = x - 38

def part_one(input_data):
    total_priority = 0
    for line in input_data:
        c1, c2 = line[:len(line)//2], line[len(line)//2:]
        total_priority += priority[list({x for x in c1} & {y for y in c2})[0]]
    return total_priority


def part_two(input_data):
    count = 0
    total_priority = 0
    lines = []
    for line in input_data:
        lines.append(line)
        if count % 3 == 2:
            l1, l2, l3 = lines
            total_priority += priority[list({x for x in l1} & {y for y in l2} & {z for z in l3})[0]]
            lines = []
        count += 1
    return total_priority


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day3.txt").read_text().strip().split('\n')
    print(part_one(DATA))
    print(part_two(DATA))
