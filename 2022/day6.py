import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def part_one(input_data):
    stream = input_data[0]
    for i in range(0, len(stream)):
        if len(set(stream[i:i+4])) == 4:
            return i + 4


def part_two(input_data):
    stream = input_data[0]
    for i in range(0, len(stream)):
        if len(set(stream[i:i+14])) == 14:
            return i + 14


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day6.txt").read_text().strip().split('\n')
    print(part_one(DATA))
    print(part_two(DATA))
