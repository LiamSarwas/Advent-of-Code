import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent

def count_trees(grid, x, y):
    trees = 0
    width = len(grid[0])
    i, j  = 0, 0
    while j < len(grid):
       trees += grid[j][i%width]
       i += x
       j += y
    return trees

def part_one(grid):
    return count_trees(grid, 3, 1)


def part_two(grid):
    trees = 1
    for x, y in [(1, 1), (3, 1), (5, 1), (7,1), (1, 2)]:
        trees *= count_trees(grid, x, y)
    return trees


if __name__ == "__main__":
    DATA = (FILE_DIR / "input"/ "day3.txt").read_text().strip().split('\n')

    grid = []
    for line in DATA:
        grid.append([0 if c == "." else 1 for c in line])

    print(part_one(grid))
    print(part_two(grid))
