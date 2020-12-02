from collections import Counter
from typing import NamedTuple
from pathlib import Path

FILE_DIR = Path(__file__).parent


class Password(NamedTuple):
    lo: int
    hi: int
    letter: str
    password: str


def part_one(passwords):
    return sum(
        [
            (password.lo <= Counter(password.password)[password.letter] <= password.hi)
            for password in passwords
        ]
    )


def part_two(passwords):
    return sum(
        [
            (password.password[password.lo - 1] == password.letter)
            != (password.password[password.hi - 1] == password.letter)
            for password in passwords
        ]
    )


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day2.txt").read_text().strip().split("\n")
    passwords = []
    for line in DATA:
        letter_range, letter, password = line.split(" ")
        lo, hi = letter_range.split("-")
        letter = letter[0]
        passwords.append(Password(int(lo), int(hi), letter, password))
    print(part_one(passwords))
    print(part_two(passwords))
