import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def part_one(input_data):
    last = input_data[0]
    increases = 0
    for depth in input_data[1:]:
        if depth > last:
            increases += 1
        last = depth
    return increases

def part_two(input_data):
    increases = 0
    for i in range(0, len(input_data) - 3):
        a = input_data[i] + input_data[i+1] + input_data[i+2]
        b = input_data[i+1] + input_data[i+2] + input_data[i+3]
        if b > a:
            increases += 1
    return increases



if __name__ == "__main__":
    DATA = [int(x) for x in (FILE_DIR / "input" / "day1.txt").read_text().strip().split('\n')]
    print(part_one(DATA))
    print(part_two(DATA))
