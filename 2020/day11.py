import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent

DATA = (FILE_DIR / "input" / "day11.txt").read_text().strip().split('\n')
w = len(DATA[0])
h = len(DATA)

COORDS = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, 1), (0, -1)]

def print_grid(grid):
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                print("#", end='')
            elif grid[i][j] == 0:
                print("L", end='')
            else:
                print(".", end='')
        print()
    print()

def is_equal(grid1, grid2):
    for i in range(h):
        for j in range(w):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True

def apply_rules(grid, i, j):
    neighbor_count = 0
    for c in COORDS:
        new_i = c[0] + i
        new_j = c[1] + j
        if 0 <= new_i < h and 0 <= new_j < w:
            if grid[new_i][new_j] == 1:
                neighbor_count += 1
    if neighbor_count == 0 and grid[i][j] == 0:
        return 1
    if neighbor_count >= 4 and grid[i][j] == 1:
        return 0
    return grid[i][j]

def apply_rules_two(grid, i, j):
    neighbor_count = 0
    for c in COORDS:
        new_i = c[0] + i
        new_j = c[1] + j
        while 0 <= new_i < h and 0 <= new_j < w:
            if grid[new_i][new_j] == 1:
                neighbor_count += 1
                break
            elif grid[new_i][new_j] == 0:
                break
            else:
                new_i = new_i + c[0]
                new_j = new_j + c[1]
    if neighbor_count == 0 and grid[i][j] == 0:
        return 1
    if neighbor_count >= 5 and grid[i][j] == 1:
        return 0
    return grid[i][j]

def advance(grid):
    next_grid = []
    for _ in range(h):
        next_grid.append([0]*w)
    for i in range(h):
        for j in range(w):
             next_grid[i][j] = apply_rules(grid, i, j)
    return next_grid

def advance_two(grid):
    next_grid = []
    for _ in range(h):
        next_grid.append([0]*w)
    for i in range(h):
        for j in range(w):
             next_grid[i][j] = apply_rules_two(grid, i, j)
    return next_grid

def part_one(grid):
    next_grid = advance(grid)
    while not is_equal(grid, next_grid):
        grid = next_grid
        next_grid = advance(grid)
        # print_grid(next_grid)
    count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                count += 1
    return count

def part_two(grid):
    next_grid = advance_two(grid)
    while not is_equal(grid, next_grid):
        grid = next_grid
        next_grid = advance_two(grid)
        # print_grid(next_grid)
    count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                count += 1
    return count


if __name__ == "__main__":
    grid = [[0 if c == "L" else 2 for c in line] for line in DATA]
    print(part_one(grid))
    print(part_two(grid))
