import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def part_one(trees):
    # visible = len(input_data[0])*2 + (len(input_data)-1)*2
    visible = 0
    seen = {}
    # top down
    for i in range(0, len(trees[0])):
        highest_seen = -1
        for j in range(0, len(trees)):
            if trees[j][i] > highest_seen:
                if (i, j) not in seen:
                    visible += 1
                    seen[(i, j)] = True
                highest_seen = trees[j][i]
    # left to right 
    for j in range(0, len(trees)):
        highest_seen = -1
        for i in range(0, len(trees[0])):
            if trees[j][i] > highest_seen:
                if (i, j) not in seen:
                    visible += 1
                    seen[(i, j)] = True
                highest_seen = trees[j][i]
    # bottom up
    for i in range(len(trees[0])-1, -1, -1):
        highest_seen = -1
        for j in range(len(trees)-1, -1, -1):
            if trees[j][i] > highest_seen:
                if (i, j) not in seen:
                    visible += 1
                    seen[(i, j)] = True
                highest_seen = trees[j][i]
    # right to left
    for j in range(len(trees)-1, -1, -1):
        highest_seen = -1
        for i in range(len(trees[0])-1, -1, -1):
            if trees[j][i] > highest_seen:
                if (i, j) not in seen:
                    visible += 1
                    seen[(i, j)] = True
                highest_seen = trees[j][i]
    return visible


def get_scenic_score(trees, h, i, j):
    l = 0
    r = 0
    u = 0
    d = 0
    x = 1
    while i - x >= 0:
        l += 1
        if h <= trees[j][i-x]:
            break
        x += 1
    x = 1
    while i + x <= len(trees[0]) - 1:
        r += 1
        if h <= trees[j][i+x]:
            break
        x += 1
    y = 1
    while j - y >= 0:
        u += 1
        if h <= trees[j-y][i]:
            break
        y += 1
    y = 1
    while j + y <= len(trees) - 1:
        d += 1
        if h <= trees[j+y][i]:
            break
        y += 1
    return l*r*u*d

def part_two(trees):
    max_scenic = 0
    for j in range(1, len(trees) - 1):
        for i in range(1, len(trees[0]) - 1):
            score = get_scenic_score(trees, trees[j][i], i, j)
            if score > max_scenic:
                max_scenic = score
    return max_scenic


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day8.txt").read_text().strip().split('\n')
    #DATA = (FILE_DIR / "input" / "day8test.txt").read_text().strip().split('\n')
    trees = []
    for line in DATA:
        tree_line = []
        for c in line:
            tree_line.append(int(c))
        trees.append(tree_line)
    print(part_one(trees))
    print(part_two(trees))
