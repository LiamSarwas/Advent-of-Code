import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def parse_seat(seat_str):
    lo, hi = 0, 127
    for i in range(0, 7):
        if seat_str[i] == "B":
            lo = (lo + hi) // 2 + 1
        else:
            hi = (lo + hi) // 2
    row = lo
    lo, hi = 0, 7
    for i in range(7, 10):
        if seat_str[i] == "R":
            lo = (lo + hi) // 2 + 1
        else:
            hi = (lo + hi) // 2
    column = lo
    return row * 8 + column


def part_one(input_data):
    return max([parse_seat(seat_str) for seat_str in input_data])


# def part_two(input_data):
#     seats = set()
#     for seat_str in input_data:
#         row, column, seat_id = parse_seat(seat_str)
#         seats.add((row, column))
# 
#     for i in range(0, 112):
#         for j in range(0, 7):
#             if (i, j) in seats:
#                 print("#", end='')
#             else:
#                 print("_", end='')
#         print(f" {i} \n")
#     im in row 82 seat 5

def part_two(input_data):
    seat_ids = [parse_seat(seat_str) for seat_str in input_data]
    lo, hi  = min(seat_ids), max(seat_ids)
    seat_ids = set(seat_ids)
    for i in range(lo + 1, hi):
        if i + 1 not in seat_ids:
            return i + 1


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day5.txt").read_text().strip().split('\n')
    print(part_one(DATA))
    print(part_two(DATA))
