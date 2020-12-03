import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def part_one(grid):
    i, j = 0, 0
    trees = 0
    width = len(grid[0])
    while j < len(grid):
       trees += grid[j][i%width]
       i += 3
       j += 1
    return trees


def part_two(input_data):
    total_trees = []
    width = len(grid[0])
    for slopes in [(1, 1), (3, 1), (5, 1), (7,1), (1, 2)]:
        trees = 0
        i, j = 0, 0
        x, y = slopes
        while j < len(grid):
           trees += grid[j][i%width]
           i += x
           j += y
        total_trees.append(trees)
    trees = 1
    for tree_count in total_trees:
        trees *= tree_count
    return trees


if __name__ == "__main__":
    DATA = (FILE_DIR / "input"/ "day3.txt").read_text().strip().split('\n')

    grid = []
    for line in DATA:
        grid.append([0 if c == "." else 1 for c in line])

    print(part_one(grid))
    print(part_two(DATA))
