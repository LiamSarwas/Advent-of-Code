import time
import itertools
import math
from pathlib import Path
import copy

FILE_DIR = Path(__file__).parent


class Monkey():
    def __init__(self, items, operation, test):
        self.items = items
        self.op = operation
        self.test = test
        self.inspected = 0

    def __str__(self):
        return f"Items: {self.items} and total inspections: {self.inspected}"

    def give(self, item):
        self.items.append(item)

def starting_monkeys():
    MONKEYS = {
        0: Monkey([91, 54, 70, 61, 64, 64, 60, 85], lambda x: x * 13, lambda y: MONKEYS[5].give(y) if y % 2 == 0 else MONKEYS[2].give(y)),
        1: Monkey([82], lambda x: x + 7, lambda y: MONKEYS[4].give(y) if y % 13 == 0 else MONKEYS[3].give(y)),
        2: Monkey([84, 93, 70], lambda x: x + 2, lambda y: MONKEYS[5].give(y) if y % 5 == 0 else MONKEYS[1].give(y)),
        3: Monkey([78, 56, 85, 93], lambda x: x * 2, lambda y: MONKEYS[6].give(y) if y % 3 == 0 else MONKEYS[7].give(y)),
        4: Monkey([64, 57, 81, 95, 52, 71, 58], lambda x: x * x, lambda y: MONKEYS[7].give(y) if y % 11 == 0 else MONKEYS[3].give(y)),
        5: Monkey([58, 71, 96, 58, 68, 90], lambda x: x + 6, lambda y: MONKEYS[4].give(y) if y % 17 == 0 else MONKEYS[1].give(y)),
        6: Monkey([56, 99, 89, 97, 81], lambda x: x + 1, lambda y: MONKEYS[0].give(y) if y % 7 == 0 else MONKEYS[2].give(y)),
        7: Monkey([68, 72], lambda x: x + 8, lambda y: MONKEYS[6].give(y) if y % 19 == 0 else MONKEYS[0].give(y))
    }
    return MONKEYS


def part_one():
    monkeys = starting_monkeys()
    for _ in range(20):
        for monkey in monkeys.values():
            while monkey.items:
                item = monkey.items.pop(0)
                monkey.inspected += 1
                new_item = monkey.op(item) // 3
                monkey.test(new_item)
    monkey_business = list(sorted([monkey.inspected for monkey in monkeys.values()], reverse=True))
    return monkey_business[0] * monkey_business[1]


def part_two():
    monkeys = starting_monkeys()
    start = time.time()
    t0 = start
    for i in range(10000):
        for monkey in monkeys.values():
            while monkey.items:
                item = monkey.items.pop(0)
                monkey.inspected += 1
                new_item = monkey.op(item) % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19)
                monkey.test(new_item)
    monkey_business = list(sorted([monkey.inspected for monkey in monkeys.values()], reverse=True))
    return monkey_business[0] * monkey_business[1]


if __name__ == "__main__":
    print(part_one())
    print(part_two())
