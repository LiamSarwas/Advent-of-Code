from collections import defaultdict
import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


def parse_rule_one(rule):
    container, contained = rule.split(" contain ")
    key = container.replace('bags', '').strip()
    values = [value.replace('bags', '').replace('bag', '').strip()[2:] for value in contained.rstrip('.').split(',')]
    return key, values

def parse_rule_two(rule):
    container, contained = rule.split(" contain ")
    key = container.replace('bags', '').strip()
    if "no other" in contained:
        return key, [(0, "empty")]
    values = [value.replace('bags', '').replace('bag', '').strip() for value in contained.rstrip('.').split(',')]
    final_values = []
    for value in values:
        num, *bag = value.split(' ')
        final_values.append((int(num), ' '.join(bag)))
    return key, final_values

def part_one(input_data):
    containable = defaultdict(set)
    for rule in input_data:
        if "no other" in rule:
            continue
        container, contained = parse_rule_one(rule)
        for bag in contained:
            containable[bag].add(container)

    shiny_gold = list(containable["shiny gold"])
    while len(shiny_gold) > 0:
        container = shiny_gold.pop(0)
        for container_container in containable[container]:
            if container_container in containable["shiny_gold"]:
                continue
            else:
                containable["shiny gold"].add(container_container)
                shiny_gold.append(container_container)
    print(len(containable["shiny gold"]))


def containing(contains, bag):
    contained_bags = contains[bag]
    if len(contained_bags) == 1 and contained_bags[0][1] == "empty":
        return 1
    else:
        bags = 0
        for bag in contained_bags:
            bags += bag[0] * containing(contains, bag[1])
        return 1 + bags


def part_two(input_data):
    rules = {}
    for rule in input_data:
        key, values = parse_rule_two(rule)
        rules[key] = values
    print(containing(rules, "shiny gold") - 1)

if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day7.txt").read_text().strip().split('\n')
    part_one(DATA)
    part_two(DATA)
