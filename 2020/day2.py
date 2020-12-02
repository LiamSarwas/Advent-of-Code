from collections import Counter
from pathlib import Path

FILE_DIR = Path(__file__).parent


def part_one(lo, hi, letter, password):
    return lo <= Counter(password)[letter] <= hi


def part_two(lo, hi, letter, password):
    return (password[lo - 1] == letter) != (password[hi - 1] == letter)


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day2.txt").read_text().strip().split("\n")
    rules = []
    for line in DATA:
        letter_range, letter, password = line.split(" ")
        lo, hi = letter_range.split("-")
        letter = letter[0]
        rules.append((int(lo), int(hi), letter, password))
    print(sum(part_one(*rule) for rule in rules))
    print(sum(part_two(*rule) for rule in rules))
