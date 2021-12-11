from itertools import product


def adjacent(p):
    incr = {p + complex(a, b) for a, b in product([-1, 0, 1], repeat=2)}
    return [i for i in incr if 0 <= i.real < 10 and 0 <= i.imag < 10]


def step(status):
    flashes = 0
    to_change = []

    for point, value in status.items():
        status[point] = (value + 1) % 10

        if status[point] == 0:
            flashes += 1
            to_change += adjacent(point)

    while len(to_change):
        point, to_change = to_change[0], to_change[1:]

        if status[point]:
            status[point] = (status[point] + 1) % 10

            if status[point] == 0:
                flashes += 1
                to_change += adjacent(point)

    return flashes


def main():
    octopus = {}

    with open('input.txt') as f:
        for r, line in enumerate(f.readlines()):
            for c, number in enumerate(line.strip()):
                octopus[c + r * 1j] = int(number)

    current_step, flashes = 0, 0

    while True:
        current_step += 1
        flashes += step(octopus)

        if current_step == 100:
            print(f'Number of flashes at step 100 (1): { flashes }')

        if sum(octopus.values()) == 0:
            break

    print(f'Synchronization step (2): { current_step }')


if __name__ == '__main__':
    main()
