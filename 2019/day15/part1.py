import time
import random
import sys
sys.path.append('..')
from collections import defaultdict, Counter
from typing import NamedTuple

from vm import IntProcessor


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)


WEST = Point(-1, 0)
EAST = Point(1, 0)
NORTH = Point(0, 1)
SOUTH = Point(0, -1)

DIRECTION = {1: NORTH, 2: SOUTH, 3: WEST, 4: EAST}


class OxygenRoom():
    def __init__(self):
        self.c_map = {0: " ", 1: ".", 2: "#", 3: "E", 4: "S"}
        self.robot = Point(0, 0)
        self.grid = {}
        self.edges = {}

    def __str__(self):
        self.grid[Point(0,0)] = 4
        min_x = min(loc.x for loc in self.grid.keys())
        max_x = max(loc.x for loc in self.grid.keys())
        min_y = min(loc.y for loc in self.grid.keys())
        max_y = max(loc.y for loc in self.grid.keys())

        print_rows = []
        for x in range(min_x, max_x + 1):
            print_row = []
            for y in range(min_y, max_y + 1):
                val = self.grid.get(Point(x, y), None)
                if val:
                    print_row.append(val)
                else:
                    print_row.append(0)
            print_rows.append(''.join(self.c_map[a] for a in print_row))
        return '\n'.join(print_rows)

    def receive_processor_output(self, i, d):
        if i == 0:
            self.grid[self.robot + DIRECTION[d]] = 2
        elif i == 1:
            self.grid[self.robot] = 1
            self.robot += DIRECTION[d]
        elif i == 2:
            self.grid[self.robot] = 1
            self.grid[self.robot + DIRECTION[d]] = 3
        else:
            print("WTF?")


def main():
    part_one = False
    with open("input") as f:
        COMMAND = [int(a) for a in f.readline().strip().split(',')]
    p = IntProcessor(COMMAND, [])
    o = OxygenRoom()

    while True:
        direction = random.randint(1, 4)
        p.memory.append(direction)
        res = p.execute()
        o.receive_processor_output(res, direction)
        print(o)
        if res == 2:
            return


if __name__ == "__main__":
    main()


# for direction in EAST, WEST, SOUTH, NORTH:
#     x = self.robot + direction
#     if x not in grid:
#         self.edges[x] = 0
