from collections import deque
import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent

def is_low_point(grid, i, j):
    if i - 1 >= 0:
        if grid[i-1][j] <= grid[i][j]:
            return False
    if i + 1 <= len(grid) - 1:
        if grid[i+1][j] <= grid[i][j]:
            return False
    if j - 1 >= 0:
        if grid[i][j-1] <= grid[i][j]:
            return False
    if j + 1 <= len(grid[0]) - 1:
        if grid[i][j+1] <= grid[i][j]:
            return False
    return True

def get_basin_size(grid, i, j):
    size = 0
    to_explore = deque([(i, j)])
    visited = set()
    while len(to_explore) > 0:
        i, j = to_explore.popleft()
        current = grid[i][j]
        size += 1
        if i - 1 >= 0 and grid[i-1][j] > current and grid[i-1][j] != 9 and (i-1, j) not in visited:
            to_explore.append((i-1, j))
            visited.add((i-1, j))
        if i + 1 <= len(grid) - 1 and grid[i+1][j] > current and grid[i+1][j] != 9 and (i+1, j) not in visited:
            to_explore.append((i+1, j))
            visited.add((i+1, j))
        if j - 1 >= 0 and grid[i][j-1] > current and grid[i][j-1] != 9 and (i, j-1) not in visited:
            to_explore.append((i, j-1))
            visited.add((i, j-1))
        if j + 1 <= len(grid) - 1 and grid[i][j+1] > current and grid[i][j+1] != 9 and (i, j+1) not in visited:
            to_explore.append((i, j+1))
            visited.add((i, j+1))
    return size

def part_one(grid):
    risk = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_low_point(grid, i, j):
                risk += 1 + grid[i][j]
    return risk

def part_two(grid):
    basins = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_low_point(grid, i, j):
                basins.append(get_basin_size(grid, i, j))
    top_3 = sorted(basins, reverse=True)[:3]
    res = 1
    for b in top_3:
        res *= b
    return res


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day9.txt").read_text().strip().split('\n')
    #DATA = (FILE_DIR / "input" / "day9test.txt").read_text().strip().split('\n')
    grid = [[int(x) for x in line] for line in DATA]
    print(part_one(grid))
    print(part_two(grid))
