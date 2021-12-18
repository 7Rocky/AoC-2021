import math
import re


def x_t(t, v0_x):
    if t > v0_x:
        return v0_x * (1 + v0_x) // 2

    return t * v0_x + t * (1 - t) // 2


def y_t(t, v0_y):
    return t * v0_y + t * (1 - t) // 2


def get_min_v0_x(x1, x2):
    min_v0_x, v0_x = math.inf, 1

    while True:
        x = v0_x * (v0_x + 1) // 2

        if x1 <= x <= x2:
            min_v0_x = min([v0_x, min_v0_x])
        if x > x2:
            break

        v0_x += 1

    return min_v0_x


def try_target(v0_x, v0_y, target, initial_velocities):
    t = 1

    while True:
        x, y = x_t(t, v0_x), y_t(t, v0_y)

        if target[0][0] <= x <= target[1][0] \
                and target[0][1] <= y <= target[1][1]:

            initial_velocities.add((v0_x, v0_y))

        if x > target[1][0] or y < target[0][1]:
            break

        t += 1


def main():
    with open('input.txt') as f:
        text = f.read().strip()

    x1, x2, y1, y2 = map(int, re.findall(
        r'target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)', text)[0])

    print(f'Maximum height possible (1): {int(abs(y1) * (abs(y1) - 1) / 2)}')

    target = ((x1, y1), (x2, y2))

    min_v0_x = get_min_v0_x(x1, x2)
    initial_velocities = set()

    for v0_x in range(min_v0_x, x2 + 1):
        for v0_y in range(-abs(y1), abs(y1)):
            try_target(v0_x, v0_y, target, initial_velocities)

    print(f'Number of initial velocities (2): {len(initial_velocities)}')


if __name__ == '__main__':
    main()
