import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def n_lcm(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        res = lcm(res, arr[i])
    return res

def part_one(estimate, busses):
    wait_time = float('inf')
    bus_taken = 0
    for bus in busses:
        r = (((estimate // bus) * bus) - estimate) + bus
        if r < wait_time:
            wait_time = r
            bus_taken = bus
    return wait_time * bus_taken

def part_two(input_data):
    t = 0
    prev_num = input_data[0]
    nums = [prev_num]
    for i, num in enumerate(input_data):
        if i == 0 or num == "x":
            continue
        target = i
        if i > num:
            target = i % num
        r = (((t // num) * num) - t) + num
        while r != target:
            t += prev_num
            r = (((t // num) * num) - t) + num
        nums.append(num)
        prev_num = n_lcm(nums)
    return t


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day13.txt").read_text().strip().split('\n')
    estimate = int(DATA[0])
    busses = [int(x) for x in DATA[1].split(',') if x != "x"]
    print(part_one(estimate, busses))
    schedule = [int(x) if x != "x" else x for x in DATA[1].split(',')]
    print(part_two(schedule))
