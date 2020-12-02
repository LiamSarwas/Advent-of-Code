from collections import Counter
import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def part_one(input_data):
    valid = 0
    for line in input_data:
        letter_range, letter, password = line.split(' ')
        lo, hi = letter_range.split('-')
        letter = letter[0]
        if int(lo) <= Counter(password)[letter] <= int(hi):
            valid += 1
    return valid

def valid_letter(letter, valid_letter):
    if letter == valid_letter:
        return True
    return False

def part_two(input_data):
    valid = 0
    for line in input_data:
        letter_range, letter, password = line.split(' ')
        letter = letter[0]
        lo, hi = letter_range.split('-')
        if valid_letter(password[int(lo)-1], letter) != valid_letter(password[int(hi)-1], letter):
            valid += 1
    return valid


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day2.txt").read_text().strip().split('\n')
    print(part_one(DATA))
    print(part_two(DATA))
