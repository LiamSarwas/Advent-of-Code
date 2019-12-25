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


LEFT = Point(-1, 0)
RIGHT = Point(1, 0)
UP = Point(0, 1)
DOWN = Point(0, -1)


def main():
    part_one = False
    with open("input") as f:
        COMMAND = [int(a) for a in f.readline().strip().split(',')]
    p = IntProcessor(COMMAND, [])

    m = ""
    while True:
        res = p.execute()
        if res == -1.5:
            print(m)
            break
        m += chr(res)
    c_map = {"#": 1, ".": 0, "^": 2}
    g = []
    for row in m.strip().split('\n'):
        g.append([c_map[c] for c in row])

    intersections = []

    for j in range(len(g)):
        for i in range(len(g[0])):
            is_int = True
            for d in LEFT, RIGHT, UP, DOWN:
               new_p = Point(i, j) + d
               if (not (0 <= new_p.x < len(g[0]))) or (not (0 <= new_p.y < len(g))):
                   is_int = False
                   break
               if g[new_p.y][new_p.x] != 1:
                   is_int = False
            if is_int:
                intersections.append(Point(i, j))

    print(sum([p.x*p.y for p in intersections]))


if __name__ == "__main__":
    main()
