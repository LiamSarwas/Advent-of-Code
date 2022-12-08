import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent

scores=  {"A": 1, "B": 2, "C": 3}


beats = {"A": "C", "B": "A", "C": "B"}
beated  = {"A": "B", "B": "C", "C": "A"}


def part_one(input_data):
    global scores
    score = 0
    for line in input_data:
        shape, response = line.split(" ")
        if response == "X":
            response = "A"
        elif response == "Y":
            response = "B"
        else:
            response = "C"
        if shape == response:
            score += 3
        elif shape == "A" and response == "C" or shape == "B" and response == "A" or shape == "C" and response == "B":
            score += 0
        else:
            score += 6
        score += scores[response]
    return score

scores=  {"A": 1, "B": 2, "C": 3}

beats = {"A": "C", "B": "A", "C": "B"}
beated  = {"A": "B", "B": "C", "C": "A"}


def part_two(input_data):
    score = 0
    for line in input_data:
        shape, response = line.split(" ")
        if response == "Y":
            response = shape
            score += 3
        elif response == "X":
            response = beats[shape]
            score += 0
        else:
            response = beated[shape]
            score += 6
        score += scores[response]
    return score


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day2.txt").read_text().strip().split('\n')
    #DATA = (FILE_DIR / "input" / "day2test.txt").read_text().strip().split('\n')

    print(part_one(DATA))
    print(part_two(DATA))
