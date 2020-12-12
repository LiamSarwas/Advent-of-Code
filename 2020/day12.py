import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent

DIRECTIONS = ["E", "S", "W", "N"]


def part_one(input_data):
    x, y = 0, 0
    direction = "E"
    for d in input_data:
        # print(f"X: {x} Y: {y} Direction: {direction}")
        if d[0] == "R":
            if d[1:] == "90":
                direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
            elif d[1:] == "180":
                direction = DIRECTIONS[(DIRECTIONS.index(direction) + 2) % 4]
            elif d[1:] == "270":
                direction = DIRECTIONS[(DIRECTIONS.index(direction) + 3) % 4]
            else:
                print("Turning right parsing error")
        if d[0] == "L":
            if d[1:] == "90":
                direction = DIRECTIONS[(DIRECTIONS.index(direction) - 1) % 4]
            elif d[1:] == "180":
                direction = DIRECTIONS[(DIRECTIONS.index(direction) - 2) % 4]
            elif d[1:] == "270":
                direction = DIRECTIONS[(DIRECTIONS.index(direction) - 3) % 4]
            else:
                print("Turning left parsing error")
        if d[0] == "F":
            if direction == "N":
                y += int(d[1:])
            if direction == "E":
                x += int(d[1:])
            if direction == "S":
                y -= int(d[1:])
            if direction == "W":
                x -= int(d[1:])
        if d[0] == "N":
            y += int(d[1:])
        if d[0] == "E":
            x += int(d[1:])
        if d[0] == "S":
            y -= int(d[1:])
        if d[0] == "W":
            x -= int(d[1:])
    return abs(x) + abs(y)


def part_two(input_data):
    x, y = 0, 0
    wx, wy = 10, 1
    for d in input_data:
        # print(f"X: {x} Y: {y}")
        if d[0] == "R":
            r = int(d[1:])
            for i in range(r//90):
                old_wx, old_wy = wx, wy
                wx = old_wy
                wy = -1 * old_wx
        if d[0] == "L":
            r = int(d[1:])
            for i in range(r//90):
                old_wx, old_wy = wx, wy
                wx = -1 * old_wy
                wy = old_wx
        if d[0] == "F":
            repeat = int(d[1:])
            x += wx * repeat
            y += wy * repeat
        if d[0] == "N":
            wy += int(d[1:])
        if d[0] == "E":
            wx += int(d[1:])
        if d[0] == "S":
            wy -= int(d[1:])
        if d[0] == "W":
            wx -= int(d[1:])
    return abs(x) + abs(y)


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day12.txt").read_text().strip().split('\n')
    print(part_one(DATA))
    print(part_two(DATA))
