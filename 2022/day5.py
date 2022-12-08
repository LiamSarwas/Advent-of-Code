import copy
import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent

#                     [L]     [H] [W]
#                 [J] [Z] [J] [Q] [Q]
# [S]             [M] [C] [T] [F] [B]
# [P]     [H]     [B] [D] [G] [B] [P]
# [W]     [L] [D] [D] [J] [W] [T] [C]
# [N] [T] [R] [T] [T] [T] [M] [M] [G]
# [J] [S] [Q] [S] [Z] [W] [P] [G] [D]
# [Z] [G] [V] [V] [Q] [M] [L] [N] [R]
#  1   2   3   4   5   6   7   8   9 


def part_one(boxes, input_data):
    for line in input_data:
        _, count, _, c1, _, c2 = line.split(" ")
        for _ in range(0, int(count)):
            boxes[int(c2)].append(boxes[int(c1)].pop())
    return "".join([c[-1] for c in boxes.values()])


def part_two(boxes, input_data):
    for line in input_data:
        _, count, _, c1, _, c2 = line.split(" ")
        crates = boxes[int(c1)][-1*int(count):]
        for c in crates:
            boxes[int(c2)].append(c)
            boxes[int(c1)].pop()
    return "".join([c[-1] for c in boxes.values()])


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day5.txt").read_text().strip().split('\n')
    initial = {
        1: ["Z", "J", "N", "W", "P", "S"],
        2: ["G", "S", "T",],
        3: ["V", "Q", "R", "L", "H"],
        4: ["V", "S", "T", "D"],
        5: ["Q", "Z", "T", "D", "B", "M", "J"],
        6: ["M", "W", "T", "J", "D", "C", "Z", "L"],
        7: ["L", "P", "M", "W", "G", "T", "J"],
        8: ["N", "G", "M", "T", "B", "F", "Q", "H"],
        9: ["R", "D", "G", "C", "P", "B", "Q", "W"]
    }
    print(part_one(copy.deepcopy(initial), DATA))
    print(part_two(copy.deepcopy(initial), DATA))
