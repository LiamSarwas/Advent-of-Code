import itertools
import math
from collections import defaultdict
from pathlib import Path

FILE_DIR = Path(__file__).parent

def update_knot(t, h):
    if abs(h[1] - t[1]) <= 1 and abs(h[0] - t[0]) <= 1:
        return t
    if h[1] == t[1]:
        if h[0] < t[0]:
            return (t[0] - 1, t[1])
        else:
            return (t[0] + 1, t[1])
    elif h[1] < t[1]:
        if h[0] < t[0]:
            return (t[0] - 1, t[1] - 1)
        elif h[0] == t[0]:
            return (t[0], t[1] - 1)
        else:
            return (t[0] + 1, t[1] - 1)
    elif h[1] > t[1]:
        if h[0] < t[0]:
            return (t[0] - 1, t[1] + 1)
        elif h[0] == t[0]:
            return (t[0], t[1] + 1)
        else:
            return (t[0] + 1, t[1] + 1)

def part_one(input_data):
    seen = defaultdict(int)
    t = (0, 0)
    h = (0, 0)
    for line in input_data:
        d, count = line.split()
        for _ in range(int(count)):
            if d == "D":
                h = (h[0], h[1] - 1)
            elif d == "U":
                h = (h[0], h[1] + 1)
            elif d == "L":
                h = (h[0] - 1, h[1])
            else:
                h = (h[0] + 1, h[1])
            t = update_knot(t, h)
            seen[t] += 1
    return len(seen.values())


def print_knots(knots):
    grid = [ [". " * 50 ] * 50]
    for i, knot in enumerate(knots):
        pass


def part_two(input_data):
    seen = defaultdict(int)
    knots = [(0, 0) for _ in range(10)]
    for line in input_data:
        d, count = line.split()
        for _ in range(int(count)):
            if d == "D":
                knots[0] = (knots[0][0], knots[0][1] - 1)
            elif d == "U":
                knots[0] = (knots[0][0], knots[0][1] + 1)
            elif d == "L":
                knots[0] = (knots[0][0] - 1, knots[0][1])
            else:
                knots[0] = (knots[0][0] + 1, knots[0][1])

            for i in range(1, 10):
                knots[i] = update_knot(knots[i], knots[i-1])
            seen[knots[9]] += 1
    return len(seen.values())


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day9.txt").read_text().strip().split('\n')
    #DATA = (FILE_DIR / "input" / "day9test.txt").read_text().strip().split('\n')
    print(part_one(DATA))
    print(part_two(DATA))
