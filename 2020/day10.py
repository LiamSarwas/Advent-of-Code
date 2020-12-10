import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent

arrangement_counts = {0: 1}

def part_one(input_data):
    adapters = [0] + sorted(input_data)
    one_diff = 0
    three_diff = 1
    for i in range(0, len(adapters) - 1):
        if adapters[i+1] - adapters[i] == 1:
            one_diff += 1
        elif adapters[i+1] - adapters[i] == 3:
            three_diff += 1
    return one_diff * three_diff

def arrangements(n, adapters):
    global arrangement_counts
    total = 0
    for i in [1, 2, 3]:
        if n - i in adapters:
            if n - i not in arrangement_counts:
                arrangement_counts[n - i] = arrangements(n - i, adapters)
            total += arrangement_counts[n - i]
    return total


def part_two(input_data):
    adapters = set(input_data + [0])
    return arrangements(max(input_data) + 3, adapters)


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day10.txt").read_text().strip().split('\n')
    DATA = [int(x) for x in DATA]
    print(part_one(DATA))
    print(part_two(DATA))
