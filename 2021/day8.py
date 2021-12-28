import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def part_one(input_data):
    return len([s for line in input_data for s in line.split(' | ')[1].split(' ') if len(s) in (2, 3, 4, 7)])

def get_digit_mapping(line):
    mapping = {}
    # pull out 1, 4, 7, 8
    remaining = []
    for w in line:
        if len(w) == 2:
            mapping[1] = w
        elif len(w) == 4:
            mapping[4] = w
        elif len(w) == 3:
            mapping[7] = w
        elif len(w) == 7:
            mapping[8] = w
        else:
            remaining.append(w)
    # pull out 0, 2, 3, 4, 7, and 9 
    new_remaining = []
    for w in remaining:
        if len(w) == 5 and mapping[1].issubset(w):
            mapping[3] = w
        elif len(w) == 5 and len(w - mapping[4]) == 3:
            mapping[2] = w
        elif len(w) == 5 and len(w - mapping[4]) == 2:
            mapping[5] = w
        elif len(w) == 6 and mapping[4].issubset(w):
            mapping[9] = w
        elif len(w) == 6 and len(w - mapping[7]) == 3:
            mapping[0] = w
        elif len(w) == 6 and len(w - mapping[7]) == 4:
            mapping[6] = w
    reverse_mapping = {}
    for key, values in mapping.items():
        reverse_mapping[frozenset(values)] = key
    return reverse_mapping

def part_two(input_data):
    total_val = 0
    for line in input_data:
        scramble, output = line.split(' | ')
        scramble = [set(s) for s in scramble.split(' ')]
        output = [frozenset(s) for s in output.split(' ')]
        m = get_digit_mapping(scramble)
        val = 0
        for i in range(0, 4):
            val += m[output[i]] * (10**(3-i))
        total_val += val
    return total_val


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day8.txt").read_text().strip().split('\n')
    print(part_one(DATA))
    print(part_two(DATA))
