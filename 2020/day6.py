from collections import Counter
import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def part_one(input_data):
    return len(sum([Counter(responses) for responses in input_data.split(' ')], Counter()))


def part_two(input_data):
    responses = input_data.split(' ')
    return len([value for value in sum([Counter(response) for response in responses], Counter()).values() if value == len(responses)])


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day6.txt").read_text().strip().split('\n\n')
    groups = [line.replace('\n', ' ') for line in DATA]
    print(sum(part_one(group) for group in groups))
    print(sum(part_two(group) for group in groups))
