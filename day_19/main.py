from collections import Counter
from itertools import product


def parse(scanner_data):
    return tuple(tuple(map(int, beacon_data.split(','))) for beacon_data in scanner_data.split('\n')[1:])


def orientate(x, y, z):
    return [(x, y, z), (z, y, -x), (-x, y, -z), (-z, y, x),
            (-y, x, z), (z, x, y), (y, x, -z), (-z, x, -y),
            (y, -x, z), (z, -x, -y), (-y, -x, -z), (-z, -x, y),
            (x, -z, y), (y, -z, -x), (-x, -z, -y), (-y, -z, x),
            (x, -y, -z), (-z, -y, -x), (-x, -y, z), (z, -y, x),
            (x, z, -y), (-y, z, -x), (-x, z, y), (y, z, x)]


def generate_orientations(beacons):
    return list(zip(*[orientate(x, y, z) for x, y, z in beacons]))


def find_overlap(absolute_beacons, scanners):
    for beacons in scanners:
        for orientation in generate_orientations(beacons):
            counter = Counter()

            for known_beacons in absolute_beacons:
                for bb in orientation:
                    counter[tuple(
                        [a - b for a, b in zip(known_beacons, bb)])] += 1

            most_common = counter.most_common(1)

            if most_common and most_common[0][1] >= 12:
                i, j, k = most_common[0][0]
                absolute_beacons_scanner = {
                    (x + i, y + j, z + k) for x, y, z in orientation}
                x, y, z = orientation[0]
                absolute_beacon = (x + i, y + j, z + k)
                absolute_scanner = tuple(
                    a - b for a, b in zip(absolute_beacon, orientation[0]))
                absolute_beacons |= absolute_beacons_scanner
                return beacons, absolute_scanner


def main():
    with open('input.txt') as f:
        beacons_scanners = [parse(l) for l in f.read().strip().split('\n\n')]

    absolute_beacons = set(beacons_scanners.pop(0))
    absolute_scanners = {(0, 0, 0)}

    while beacons_scanners:
        found_beacon, absolute_scanner = find_overlap(
            absolute_beacons, beacons_scanners)
        absolute_scanners.add(absolute_scanner)
        beacons_scanners.remove(found_beacon)

    print(f'Number of beacons (1):', len(absolute_beacons))

    d = 0

    for A, B in product(absolute_scanners, absolute_scanners):
        d = max(d, sum(abs(a - b) for a, b in zip(A, B)))

    print('Largest distance (2):', d)


if __name__ == '__main__':
    main()
