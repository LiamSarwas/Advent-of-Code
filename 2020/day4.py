import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def make_passport(string):
    passport = {}
    for field in string.split(" "):
        key, value = field.split(":")
        passport[key] = value
    return passport


def part_one(passport):
    if "byr" not in passport:
        return False
    if "iyr" not in passport:
        return False
    if "eyr" not in passport:
        return False
    if "hgt" not in passport:
        return False
    if "hcl" not in passport:
        return False
    if "ecl" not in passport:
        return False
    if "pid" not in passport:
        return False
    return True


def part_two(passport):
    try:
        if "byr" not in passport:
            return False
        else:
            byr = int(passport["byr"])
            if byr < 1920 or byr > 2002:
                return False
        if "iyr" not in passport:
            return False
        else:
            iyr = int(passport["iyr"])
            if iyr < 2010 or iyr > 2020:
                return False
        if "eyr" not in passport:
            return False
        else:
            eyr = int(passport["eyr"])
            if eyr < 2020 or eyr > 2030:
                return False
        if "hgt" not in passport:
            return False
        else:
            hgt = passport["hgt"]
            hgt_num = int(hgt[:-2])
            if "cm" in hgt:
                if hgt_num < 150 or hgt_num > 193:
                    return False
            if "in" in hgt:
                if hgt_num < 59 or hgt_num > 76:
                    return False
        if "hcl" not in passport:
            return False
        else:
            hcl = passport["hcl"]
            if hcl[0] != "#":
                return False
            if len(hcl[1:]) != 6:
                return False
            for c in hcl[1:]:
                if c not in [
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "a",
                    "b",
                    "c",
                    "d",
                    "e",
                    "f",
                ]:
                    return False
        if "ecl" not in passport:
            return False
        else:
            ecl = passport["ecl"]
            if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
        if "pid" not in passport:
            return False
        else:
            pid = passport["pid"]
            if len(pid) != 9:
                return False
            pid = int(pid)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day4.txt").read_text().strip().split("\n\n")
    passports = []
    for line in DATA:
        passport = make_passport(line.replace("\n", " "))
        passports.append(passport)
    print(sum(part_one(passport) for passport in passports))
    print(sum(part_two(passport) for passport in passports))
