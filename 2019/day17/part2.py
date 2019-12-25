import time
import random
import sys
sys.path.append('..')
from collections import defaultdict, Counter
from typing import NamedTuple

from vm import IntProcessor


def main():
    # part2 - solved mainly by hand
    with open("input2") as f:
        COMMAND = [int(a) for a in f.readline().strip().split(',')]
    p = IntProcessor(COMMAND, [])

    i = ("B,C,B,A,C,A,B,A,C,A\n" +
        "L,4,L,6,L,8,L,8\n" +
        "L,8,R,10,L,10\n" +
        "R,10,L,8,L,8,L,10\n" +
        "n\n")
    for c in i:
        p.memory.append(ord(c))

    while True:
        res = p.execute()
        if res == -1.5:
            break
        elif res < 256:
            print(chr(res), end='')
        else:
            print(res)


if __name__ == "__main__":
    main()
