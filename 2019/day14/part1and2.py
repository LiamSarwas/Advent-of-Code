import math
from collections import defaultdict


def parse_input():
    recipes = {}
    with open("input") as f:
        for line in f:
            i, o = line.strip().split(" => ")
            inputs = []
            for chemical in i.strip().split(","):
                c, name = chemical.strip().split(" ")
                inputs.append((int(c), name))
            c, name = o.split(" ")
            recipes[name] = (int(c), inputs)
    return recipes


def produce(name):
    recipe = recipes[name]
    # how many of the incoming component do I have left to produce?
    count = math.ceil(max(0, needed[name] - producing[name]) / recipe[0])
    # produce that many
    producing[name] += count * recipe[0]
    for component in recipe[1]:
        # add all the components that we need to produce 
        needed[component[1]] += count * component[0]

    for component in recipe[1]:
        if component[1] != "ORE":
            # recurse to all of the non-ore components and produce them
            produce(component[1])


recipes = parse_input()
needed = defaultdict(int)
producing = defaultdict(int)

def main():
    # part 1
    needed["FUEL"] = 1
    produce("FUEL")
    print(needed["ORE"])

    # part 2
    # did manual binary search
    needed["FUEL"] = 2390226
    produce("FUEL")
    print(needed["ORE"])

if __name__ == "__main__":
    main()
