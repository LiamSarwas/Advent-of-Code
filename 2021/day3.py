import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def most_common_bit(d, i):
    c = 0
    for l in d:
        if l[i] == "1":
            c += 1
        else:
            c -= 1
    if c >= 0:
        return "1"
    return "0"

def least_common_bit(d, i):
    c = 0
    for l in d:
        if l[i] == "1":
            c += 1
        else:
            c -= 1
    if c >= 0:
        return "0"
    return "1"

def part_one(input_data):
    common = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
    #common  = [0,0,0,0,0]
    for l in input_data:
        for i, c in enumerate(l):
            if c == "1":
                common[i] += 1
            else:
                common[i] -= 1
    g = ""
    e = ""
    for c in common:
        if c < 0:
            g += "0"
            e += "1"
        elif c > 0:
            g += "1"
            e += "0"
        else:
            print("invalid: neither 0,1 more common")
    g = int(g, 2)
    e = int(e, 2)
    return g*e

def part_two(input_data):
    d = input_data
    bit = 0
    while len(d) > 1:
        mc = most_common_bit(d, bit)
        new_d = []
        for n in d:
            if n[bit] == mc:
                new_d.append(n)
        bit += 1
        d = new_d
    o = int(d[0], 2)

    d = input_data
    bit = 0
    while len(d) > 1:
        lc = least_common_bit(d, bit)
        new_d = []
        for n in d:
            if n[bit] == lc:
                new_d.append(n)
        bit += 1
        d = new_d
    c = int(d[0], 2)
    return o*c


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day3.txt").read_text().strip().split('\n')
    #DATA = (FILE_DIR / "input" / "day3test.txt").read_text().strip().split('\n')
    print(part_one(DATA))
    print(part_two(DATA))
