import itertools
import math
from pathlib import Path
from collections import defaultdict
import time

FILE_DIR = Path(__file__).parent


def solve(input_data, target):
    num_pos = defaultdict(list)
    for i in range(1, len(input_data) + 1):
        num_pos[input_data[i-1]].append(i)
    last_said = input_data[-1]
    new_num = True
    i += 1
    while i <= target:
        if new_num:
            last_said = 0
            num_pos[0].append(i)
            new_num = False
        else:
            diff = num_pos[last_said][-1] - num_pos[last_said][-2]
            last_said = diff
            if diff in num_pos:
                new_num = False
            else:
                new_num = True
            num_pos[diff].append(i)
        i += 1
    return last_said


if __name__ == "__main__":
    DATA = [16,11,15,0,1,7]
    print(solve(DATA, 2020))
    print(solve(DATA, 30000000))
