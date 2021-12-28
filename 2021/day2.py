import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def part_one(input_data):
    d = 0
    h = 0
    for l in input_data:
        c, v = l.split(' ')
        v = int(v)
        if c == "forward":
            h += v
        elif c == "down":
            d += v
        elif c == "up":
            d -= v
        else:
            print("invalid input")
    return d*h


def part_two(input_data):
    d = 0
    h = 0
    a = 0
    for l in input_data:
        c, v = l.split(' ')
        v = int(v)
        if c == "forward":
            h += v
            d += v*a
        elif c == "down":
            a += v
        elif c == "up":
            a -= v
        else:
            print("invalid input")
    return d*h


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day2.txt").read_text().strip().split('\n')
    print(part_one(DATA))
    print(part_two(DATA))
