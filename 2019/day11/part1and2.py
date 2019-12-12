import sys
sys.path.append('..')
from enum import Enum
from collections import namedtuple, defaultdict

from vm import IntProcessor


Point = namedtuple("Point", ["x", "y"])

LEFT = Point(-1, 0)
RIGHT = Point(1, 0)
UP = Point(0, 1)
DOWN = Point(0, -1)


class PaintBot():
    def __init__(self):
        self.rotation = UP
        self.location = Point(0, 0)
        self.rotate_right = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}
        self.rotate_left = {UP: LEFT, LEFT: DOWN, DOWN: RIGHT, RIGHT: UP}
        self.grid = defaultdict(bool)

    def __str__(self):
        min_x = min(loc.x for loc in self.grid.keys())
        max_x = max(loc.x for loc in self.grid.keys())
        min_y = min(loc.y for loc in self.grid.keys())
        max_y = max(loc.y for loc in self.grid.keys())

        print_rows = []
        for x in range(min_x, max_x + 1):
            print_row = []
            for y in range(min_y, max_y + 1):
                if self.grid.get(Point(x, y), None) == True:
                    print_row.append(1)
                else:
                    print_row.append(0)
            print_rows.append(''.join("X" if a else " " for a in print_row))
        return '\n'.join(print_rows)

    def receive_input(self, p, r):
        self._paint(p)
        self._rotate(r)
        self._move()
        return self.grid[self.location]

    def _rotate(self, r: bool):
        if r:
            self.rotation = self.rotate_right[self.rotation]
        else:
            self.rotation = self.rotate_left[self.rotation]

    def _paint(self, val):
        if val:
            self.grid[self.location] = True
        else:
            self.grid[self.location] = False

    def _move(self):
        self.location = Point(self.location.x + self.rotation.x, self.location.y + self.rotation.y)
        if self.location not in self.grid:
            self.grid[self.location] = False


def main():
    part_one = False
    COMMAND = []
    with open("input") as f:
        COMMAND = [int(a) for a in f.readline().strip().split(',')]
    if part_one:
        proc = IntProcessor(COMMAND, [0])
    else:
        proc = IntProcessor(COMMAND, [1])
    bot = PaintBot()
    while True:
        proc_out = []
        proc_term = False
        while True:
            result = proc.execute()
            if result == -2:
                break
            elif result == -1.5:
                proc_term = True
                break
            else:
                proc_out.append(result)
        if len(proc_out) == 2:
            new_color = bot.receive_input(proc_out[0], proc_out[1])
            proc.memory.append(new_color)
        else:
            print("Unexpected branch: WTF?")
        if proc_term:
            break

    print(f"PaintBot painted {len(bot.grid)} squares at least once")
    print(bot)


if __name__ == "__main__":
    main()
