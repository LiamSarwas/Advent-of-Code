from collections import defaultdict
import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent

def print_grid(points):
    y = max([p[0] for p in points.keys()])
    x = max([p[1] for p in points.keys()])
    for j in range(x+1):
        for i in range(y+1):
            if (i, j) in points:
                print(f"{points[(i, j)]} ", end = '')
            else:
                print(f". ", end = '')
        print()

def parse_line(l):
    a, b = l.split(' -> ')
    x1, y1 = a.split(',')
    x2, y2 = b.split(',')
    return (int(x1), int(y1)), (int(x2), int(y2))

def part_one(input_data):
    p = defaultdict(int)
    for line in input_data:
        a, b = parse_line(line)
        if a[0] == b[0]:
            if a[1] <= b[1]:
                for i in range(a[1], b[1]+1):
                    p[(a[0], i)] += 1
            else:
                for i in range(b[1], a[1]+1):
                    p[(a[0], i)] += 1
        elif a[1] == b[1]:
            if a[0] <= b[0]:
                for i in range(a[0], b[0]+1):
                    p[(i, a[1])] += 1
            else:
                for i in range(b[0], a[0]+1):
                    p[(i, a[1])] += 1

    count = 0
    for _, value in p.items():
        if value >= 2:
            count += 1
    return count

def part_two(input_data):
    p = defaultdict(int)
    for line in input_data:
        a, b = parse_line(line)
        if a[0] == b[0] and a[1] != b[1]:
            if a[1] <= b[1]:
                for i in range(a[1], b[1]+1):
                    p[(a[0], i)] += 1
            else:
                for i in range(b[1], a[1]+1):
                    p[(a[0], i)] += 1
        elif a[1] == b[1] and a[0] != b[0]:
            if a[0] <= b[0]:
                for i in range(a[0], b[0]+1):
                    p[(i, a[1])] += 1
            else:
                for i in range(b[0], a[0]+1):
                    p[(i, a[1])] += 1
        elif abs(a[0] - b[0]) == abs(a[1] - b[1]):
            diff = abs(b[0] - a[0])
            x_vals = []
            if a[0] <= b[0]:
                for i in range(diff + 1):
                    x_vals.append(a[0] + i)
            else:
                for i in range(diff + 1):
                    x_vals.append(a[0] - i)
            y_vals = []
            if a[1] <= b[1]:
                for i in range(diff + 1):
                    y_vals.append(a[1] + i)
            else:
                for i in range(diff + 1):
                    y_vals.append(a[1] - i)
            points = zip(x_vals, y_vals)
            for point in points:
                p[(point[0], point[1])] += 1
    #print_grid(p)
    count = 0
    for _, value in p.items():
        if value >= 2:
            count += 1
    return count

if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day5.txt").read_text().strip().split('\n')
    #DATA = (FILE_DIR / "input" / "day5test.txt").read_text().strip().split('\n')
    print(part_one(DATA))
    print(part_two(DATA))
