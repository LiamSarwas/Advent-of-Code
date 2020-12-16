import itertools
import math
from pathlib import Path
from collections import defaultdict

FILE_DIR = Path(__file__).parent

def parse_rules(line):
    rule_name, ranges = line.split(': ')
    lo, hi = ranges.split(" or ")
    a, b  = lo.split('-')
    c, d  = hi.split('-')
    print(rule_name)
    return rule_name, (int(a), int(b)), (int(c), int(d))


def part_one(rule_ranges, tickets):
    valid = set()
    for rule in rule_ranges:
        for num in range(rule[1], rule[2]+1):
            valid.add(num)
    error_rate = 0
    valid_tickets = []
    for ticket in tickets:
        valid_ticket = True
        for field in ticket:
            if field not in valid:
                error_rate += field
                valid_ticket = False
        if valid_ticket:
            valid_tickets.append(ticket)
    return error_rate, valid_tickets


def valid_for(rules, rule_names, solved, field):
    fields = set()
    for rule_name in rule_names:
        if rule_name in solved:
            continue
        if field in rules[rule_name]:
            fields.add(rule_name)
    return fields

def part_two(rule_ranges, valid_tickets):
    names = set()
    rules = defaultdict(set)
    for rule in rule_ranges:
        name, lo, hi = rule
        for i in range(lo, hi + 1):
            rules[name].add(i)
            names.add(name)
    solved_columns = set()
    departure_fields = []
    while solved_columns != names:
        for column in range(0, 20):
            fields = set(names)
            for ticket in valid_tickets:
                valid_fields = valid_for(rules, names, solved_columns, ticket[column])
                fields = set.intersection(fields, valid_fields)
            if len(fields) == 1:
                solved_columns = solved_columns.union(fields)
                for field in fields:
                    if field.startswith("departure"):
                        departure_fields.append(column)
                print(f"Column {column} is valid for rules: {fields}")
    return departure_fields


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day16.txt").read_text().strip().split('\n')
    rule_ranges = []
    for i in range(20):
        rule_name, range_one, range_two = parse_rules(DATA[i])
        rule_ranges.append((rule_name, *range_one))
        rule_ranges.append((rule_name, *range_two))
    my_ticket = [int(num) for num in DATA[22].split(',')]
    nearby_tickets = [[int(num) for num in DATA[j].split(',')] for j in range(25, len(DATA))]
    error_rate, valid_tickets = part_one(rule_ranges, nearby_tickets)
    print(error_rate)
    departure_fields = part_two(rule_ranges, valid_tickets)
    answer = 1
    for field in departure_fields:
        answer *= my_ticket[field]
    print(answer)
