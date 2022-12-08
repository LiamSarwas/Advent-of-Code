import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def part_one(input_data):
    count = 0
    for line in input_data:
        c1, c2 = line.split(",")
        s1, s2 = c1.split("-")
        r1 = {x for x in range(int(s1), int(s2)+1)}
        s1, s2 = c2.split("-")
        r2 = {x for x in range(int(s1), int(s2)+1)}
        if r1.issubset(r2) or r2.issubset(r1):
            count += 1
    return count


def part_two(input_data):
    count = 0
    for line in input_data:
        c1, c2 = line.split(",")
        s1, s2 = c1.split("-")
        r1 = {x for x in range(int(s1), int(s2)+1)}
        s1, s2 = c2.split("-")
        r2 = {x for x in range(int(s1), int(s2)+1)}
        if r1 & r2:
            count += 1
    return count


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day4.txt").read_text().strip().split('\n')
    print(part_one(DATA))
    print(part_two(DATA))
