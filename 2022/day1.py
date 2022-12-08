import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def part_one(input_data):
    return max([sum(bag) for bag in input_data])


def part_two(input_data):
    return sum(sorted([sum(bag) for bag in input_data], reverse=True)[:3])


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day1.txt").read_text().strip().split('\n')
    elves = []
    current_bag = []
    for line in DATA:
        if line == "":
            elves.append(current_bag)
            current_bag = []
        else:
            current_bag.append(int(line))

    print(part_one(elves))
    print(part_two(elves))
