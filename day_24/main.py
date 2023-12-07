from itertools import product

adds_x, adds_y = [], []
divs = set()


def monad(input_numbers):
    x, z = 0, 0

    for i, number in enumerate(input_numbers):
        x = z % 26
        z //= 26 if i in divs else 1
        x += adds_x[i]
        x = int(x != number)
        z *= 25 * x + 1
        z += (number + adds_y[i]) * x

    return z


def make_number(p):
    return [
        p[0],
        p[1],
        p[2],
        p[3],
        p[4],
        p[4] + adds_y[4] + adds_x[5],
        p[3] + adds_y[3] + adds_x[6],
        p[5],
        p[5] + adds_y[7] + adds_x[8],
        p[6],
        p[6] + adds_y[9] + adds_x[10],
        p[2] + adds_y[2] + adds_x[11],
        p[1] + adds_y[1] + adds_x[12],
        p[0] + adds_y[0] + adds_x[13]
    ]


def main():
    with open('input.txt') as f:
        for i, line in enumerate(f.read().splitlines()):
            if line == 'div z 26':
                divs.add(i // 18)
            if i % 18 == 5:
                adds_x.append(int(line[6:]))
            if i % 18 == 15:
                adds_y.append(int(line[6:]))

    for number in map(make_number, product(*[range(9, -1, -1) for _ in range(7)])):
        if all(map(lambda n: 0 < n < 10, number)) and monad(number) == 0:
            print('Greatest MONAD (1):', ''.join(map(str, number)))
            break

    for number in map(make_number, product(*[range(1, 10) for _ in range(7)])):
        if all(map(lambda n: 0 < n < 10, number)) and monad(number) == 0:
            print('Smallest MONAD (2):', ''.join(map(str, number)))
            break


if __name__ == '__main__':
    main()
