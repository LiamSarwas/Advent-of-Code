import sys
sys.path.append('..')
from vm import IntProcessor


def main():
    part_one = False
    with open("input") as f:
        COMMAND = [int(a) for a in f.readline().strip().split(',')]
    if part_one:
        p = IntProcessor(COMMAND, [1])
    else:
        p = IntProcessor(COMMAND, [2])
    while True:
        result = p.execute()
        if result != -1.5:
            print(result)
        else:
            break


if __name__  == "__main__":
    main()
