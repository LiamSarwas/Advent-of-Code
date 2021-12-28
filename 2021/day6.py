from collections import Counter, defaultdict
import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent

def part_one(input_data):
    fish = [int(x) for x in input_data.split(',')]
    for i in range(80):
        new_fish = []
        for f in fish:
            if f == 0:
                new_fish.append(6)
                new_fish.append(8)
            else:
                new_fish.append(f-1)
        fish = new_fish
    return len(fish)


def part_two(input_data):
    fish = [int(x) for x in input_data.split(',')]
    c = Counter(fish)
    for i in range(256):
        new_c = defaultdict(int)
        for i in range(9):
            if i == 0:
                new_c[6] += c[i]
                new_c[8] += c[i]
            else:
                new_c[i-1] += c[i]
        c = new_c
    return sum([v for v in c.values()])

if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day6.txt").read_text().strip().split('\n')
    print(part_one(DATA[0]))
    print(part_two(DATA[0]))
