import re

from itertools import product
from math import prod


p = r'[xyz]=(-?\d+)\.\.(-?\d+)'


def get_coordinates(coordinates):
    return (list(map(int, t)) for t in re.findall(p, coordinates))


def step(cores, s):
    status, coordinates = s.split()
    x, y, z = get_coordinates(coordinates)

    a = map(lambda t: max([-50, t[0]]), [x, y, z])
    b = map(lambda t: min([50, t[1]]) + 1, [x, y, z])

    for c in product(*map(range, a, b)):
        cores[c] = status == 'on'


def intersect(a, b):
    c = {
        'm': -a['m'],
        'c': {d: [max(a['c'][d][0], b['c'][d][0]), min(a['c'][d][1], b['c'][d][1])] for d in 'xyz'}
    }

    return {} if any(c['c'][d][0] > c['c'][d][1] for d in 'xyz') else c


def main():
    with open('input.txt') as f:
        steps = f.readlines()

    cores = {}

    for s in steps:
        step(cores, s)

    print(f'Number of cubes on (1): {sum(cores.values())}')

    cores = []

    for s in steps:
        status, coordinates = s.split()
        x, y, z = get_coordinates(coordinates)

        mode = 1 if status == 'on' else -1
        cuboid = {'m': mode, 'c': dict(zip('xyz', [x, y, z]))}
        to_add = [cuboid] if mode == 1 else []

        for core in cores:
            intersection = intersect(core, cuboid)

            if intersection:
                to_add.append(intersection)

        cores += to_add

    count = sum(c['m'] * prod(c['c'][d][1] - c['c'][d][0] + 1 for d in 'xyz')
                for c in cores)

    print(f'Number of cubes on (2): {count}')


if __name__ == '__main__':
    main()
