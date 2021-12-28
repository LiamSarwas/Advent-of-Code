import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def cost(n):
    return (n*(n+1))//2

def part_one(input_data):
    # this shouldn't have worked but I got lucky
    p = [int(x) for x in input_data.split(',')]
    min_cost = max(p)**2
    for i in range(0, len(p)):
        total_cost = 0
        for j in range(0, len(p)):
            if i == j:
                pass
            total_cost += abs(p[i] - p[j])
        if total_cost < min_cost:
            min_cost = total_cost
    return min_cost


def part_two(input_data):
    p = [int(x) for x in input_data.split(',')]
    min_cost = 10000000000000000
    for i in range(0, max(p)):
        total_cost = 0
        for j in range(0, len(p)):
            if i == j:
                pass
            total_cost += cost(abs(i - p[j]))
        if total_cost <= min_cost:
            min_cost = total_cost
    return min_cost


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day7.txt").read_text().strip().split('\n')
    #DATA = ["16,1,2,0,4,2,7,1,2,14"]
    print(part_one(DATA[0]))
    print(part_two(DATA[0]))
