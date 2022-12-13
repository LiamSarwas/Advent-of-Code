import itertools
import math
from pathlib import Path
import functools

FILE_DIR = Path(__file__).parent

def compare_list(a, b):
    left_shorter = True
    if len(b) <= len(a):
        left_shorter = False
    if left_shorter:
        for i in range(len(a)):
            if isinstance(a[i], int) and isinstance(b[i], int):
                if a[i] < b[i]:
                    return 1
                elif a[i] > b[i]:
                    return -1
                else:
                    continue
            if isinstance(a[i], list) and isinstance(b[i], list):
               value = compare_list(a[i], b[i])
               if value == 1:
                   return 1
               elif value == -1:
                   return -1
               else:
                   continue
            if isinstance(a[i], int):
               value = compare_list([a[i]], b[i])
               if value == 1:
                   return 1
               elif value == -1:
                   return -1
               else:
                   continue
            if isinstance(b[i], int):
               value = compare_list(a[i], [b[i]])
               if value == 1:
                   return 1
               elif value == -1:
                   return -1
               else:
                   continue
        return 1
    else:
        for i in range(len(b)):
            if isinstance(a[i], int) and isinstance(b[i], int):
                if a[i] < b[i]:
                    return 1
                elif a[i] > b[i]:
                    return -1
                else:
                    continue
            if isinstance(a[i], list) and isinstance(b[i], list):
               value = compare_list(a[i], b[i])
               if value == 1:
                   return 1
               elif value == -1:
                   return -1
               else:
                   continue
            if isinstance(a[i], int):
               value = compare_list([a[i]], b[i])
               if value == 1:
                   return 1
               elif value == -1:
                   return -1
               else:
                   continue
            if isinstance(b[i], int):
               value = compare_list(a[i], [b[i]])
               if value == 1:
                   return 1
               elif value == -1:
                   return -1
               else:
                   continue
    if len(a) == len(b):
        return 0
    return -1


def part_one(input_data):
    total = 0
    for i in range(0, len(input_data)):
        left = input_data[i][0]
        right = input_data[i][1]
        if compare_list(left, right) == 1:
            total += (i + 1)
    return total


def part_two(input_data):
    answer = 1
    for i, packet in enumerate(sorted(input_data, key=functools.cmp_to_key(compare_list), reverse=True)):
        print(i + 1, packet)
        if packet == [[2]] or packet == [[6]]:
            answer *= i+1
    return answer



if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day13.txt").read_text().strip().split('\n')
    # DATA = (FILE_DIR / "input" / "day13test.txt").read_text().strip().split('\n')
    pairs = []
    pair = []
    for line in DATA:
        if line == '':
            pairs.append(pair)
            pair = []
        else:
            pair.append(eval(line))
    print(part_one(pairs))
    dividers = [[[2]],[[6]]]
    packets = [*dividers]
    for line in DATA:
        if line == '':
            continue
        packets.append(eval(line))
    print(part_two(packets))
