from itertools import combinations
from typing import NamedTuple


class Velocity(NamedTuple):
    x: int
    y: int
    z: int

    def __add__(self, v):
        return Velocity(self.x + v.x, self.y + v.y, self.z + v.z)


class Position(NamedTuple):
    x: int
    y: int
    z: int

    def __add__(self, v):
        return Position(self.x + v.x, self.y + v.y, self.z + v.z)


class Moon():
    def __init__(self, x, y, z):
        self.position = Position(x, y, z)
        self.velocity = Velocity(0, 0, 0)

    def total_energy(self):
        pe = sum(abs(p) for p in self.position)
        ke = sum(abs(v) for v in self.velocity)
        return pe * ke


def calc_gravity(m1, m2):
    if m1.x == m2.x:
        m1_x = 0
        m2_x = 0
    elif m1.x < m2.x:
        m1_x = 1
        m2_x = -1
    else:
        m1_x = -1
        m2_x = 1

    if m1.y == m2.y:
        m1_y = 0
        m2_y = 0
    elif m1.y < m2.y:
        m1_y = 1
        m2_y = -1
    else:
        m1_y = -1
        m2_y = 1

    if m1.z == m2.z:
        m1_z = 0
        m2_z = 0
    elif m1.z < m2.z:
        m1_z = 1
        m2_z = -1
    else:
        m1_z = -1
        m2_z = 1
    return Velocity(m1_x, m1_y, m1_z), Velocity(m2_x, m2_y, m2_z)


def apply_gravity(moons, bodies=2):
    for moon_a, moon_b in combinations(moons, bodies):
        moon_a_v, moon_b_v = calc_gravity(moon_a.position, moon_b.position)
        moon_a.velocity += moon_a_v
        moon_b.velocity += moon_b_v


def main():
    moons_input = [(0, 4, 0), (-10, -6, -14), (9, -16, -3), (6, -1, 2)]
    moons = [Moon(*moon) for moon in moons_input]

    for i in range(0, 1000):
        apply_gravity(moons)
        for m in moons:
            m.position += m.velocity

    print(sum(m.total_energy() for m in moons))


if __name__ == "__main__":
    main()
