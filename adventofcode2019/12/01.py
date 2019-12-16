import os
import re
from itertools import combinations

os.chdir('/home/alexx/github/puzzles/adventofcode2019/12')


class Moon():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    def __repr__(self):
        return (f'Moon at ({self.x}, {self.y}, {self.z}), '
                f'velocities ({self.vel_x}, {self.vel_y}, {self.vel_z})'
                )

    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kinetic_energy(self):
        return abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()


class System():
    def __init__(self, list_of_moons, debug=False):
        self.moons = []
        self.debug = debug
        for moon in list_of_moons:
            assert isinstance(moon, Moon)
            self.moons += [moon]
        self.time = 0

    def __str__(self):
        res = f'After {self.time} steps: \n'
        for moon in self.moons:
            res += f'pos=<x={moon.x}, y={moon.y}, z={moon.z}>, '
            res += f'vel=<x={moon.vel_x}, y={moon.vel_y}, z={moon.vel_z}>\n'
        res += '\n'
        return res

    def step(self):
        # Apply gravity, i.e. update velocities
        for moon_1, moon_2 in combinations(self.moons, 2):
            if moon_1.x < moon_2.x:
                moon_1.vel_x += 1
                moon_2.vel_x -= 1
            elif moon_1.x > moon_2.x:
                moon_1.vel_x -= 1
                moon_2.vel_x += 1
            # else, both x positions are the same. Don't update the x-velocity.
            if moon_1.y < moon_2.y:
                moon_1.vel_y += 1
                moon_2.vel_y -= 1
            elif moon_1.y > moon_2.y:
                moon_1.vel_y -= 1
                moon_2.vel_y += 1
            if moon_1.z < moon_2.z:
                moon_1.vel_z += 1
                moon_2.vel_z -= 1
            elif moon_1.z > moon_2.z:
                moon_1.vel_z -= 1
                moon_2.vel_z += 1

        # Apply velocities, i.e. update positions
        for moon in self.moons:
            moon.x += moon.vel_x
            moon.y += moon.vel_y
            moon.z += moon.vel_z

        self.time += 1

    def get_total_energy(self):
        total_energy = 0
        if self.debug:
            print(f'Energy after {self.time} steps:')
        for x in self.moons:
            res = f'Pot: {x.potential_energy()}'
            res += f', Kin: {x.kinetic_energy()}'
            res += f', Tot: {x.total_energy()}'
            if self.debug:
                print(res)
            total_energy += x.total_energy()

        return total_energy


with open('input') as f:
    io = Moon(*map(int, re.findall(r'=(-?\d+)', f.readline())))
    europa = Moon(*map(int, re.findall(r'=(-?\d+)', f.readline())))
    ganymede = Moon(*map(int, re.findall(r'=(-?\d+)', f.readline())))
    callisto = Moon(*map(int, re.findall(r'=(-?\d+)', f.readline())))

print(europa)

system = System([io, europa, ganymede, callisto])
#print(system)

for i in range(1000):
    system.step()
    #print(system)

print(system.get_total_energy())
