import time
import sys
sys.path.append('..')
from collections import defaultdict, Counter
from typing import NamedTuple

from vm import IntProcessor


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)


class Entity(NamedTuple):
    p: Point
    t: int


class GameBoard():
    def __init__(self, entities):
        self.c_map = {0: " ", 1: "X", 2: "#", 3: "_", 4: "o"}
        self.paddle = Point(0, 0)
        self.ball = Point(0, 0)
        self.grid = [ [0]*43 for _ in range(22) ]
        for e in entities:
            self.grid[e.p.y][e.p.x] = e.t
            if e.t == 3:
                self.paddle = e.p
            if e.t == 4:
                self.ball = e.p
        self.score = ""

    def __str__(self):
        print_str = '\n'.join([''.join([self.c_map[a] for a in row]) for row in self.grid])
        print_str += '\rX  ' + self.score + '\n'
        return print_str

    def update(self, e):
        if e.p.x == -1 and e.p.y == 0:
            self.score = str(e.t)
        else:
            if e.t == 3:
                self.paddle = e.p
            if e.t == 4:
                self.ball = e.p
            self.grid[e.p.y][e.p.x] = e.t

    def get_next_move(self):
        if self.paddle.x < self.ball.x:
            return 1
        elif self.paddle.x > self.ball.x:
            return -1
        else:
            return 0


def main():
    part_one = False
    with open("input") as f:
        COMMAND = [int(a) for a in f.readline().strip().split(',')]
    p = IntProcessor(COMMAND, [])
    c = 0
    triplets = []
    while True:
        triplet = []
        for i in range(0, 3):
            triplet.append(p.execute())
        if triplet[2] == 2:
            c += 1
        if -1.5 in triplet:
            print(c)
            break
        else:
            triplets.append(triplet)
    if part_one:
        return

    entities = [Entity(Point(t[0], t[1]), t[2]) for t in triplets]
    g = GameBoard(entities)
    print(g)
    COMMAND[0] = 2
    p = IntProcessor(COMMAND, [])
    t = []
    while True:
        res = p.execute()
        if res == -2.5:
            #js = int(input("Which way to move joystick (1, 2, 3)?"))
            #if js == 1:
            #    js = -1
            #if js == 2:
            #    js = 0
            #if js == 3:
            #    js = 1
            js = g.get_next_move()
            print(js)
            p.memory.append(js)
        elif res == -1.5:
            print(g)
            print("Game over!")
            return
        else:
            t.append(res)
            if len(t) == 3:
                e = Entity(Point(t[0], t[1]), t[2])
                g.update(e)
                print(g)
                t = []


if __name__ == "__main__":
    main()
