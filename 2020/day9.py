import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def part_one(input_data):
    i = 25
    preamble = input_data[:i]
    while i < len(input_data):
        for c in itertools.combinations(preamble, 2):
            if (c[0] + c[1]) == input_data[i]:
                break
        else:
            return input_data[i]
        preamble.pop(0)
        preamble.append(input_data[i])
        i += 1


def part_two(target, input_data):
    for i in range(len(input_data) - 1):
        num = input_data[i]
        j = i + 1
        while num < target:
            num += input_data[j]
            if num == target:
                return min(input_data[i:j+1]) + max(input_data[i:j+1])
            else:
                j += 1


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day9.txt").read_text().strip().split('\n')
    DATA = [int(x) for x in DATA]
    print(part_one(DATA))
    num  = 731031916
    print(part_two(num, DATA))
