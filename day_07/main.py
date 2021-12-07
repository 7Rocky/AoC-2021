def fuel_constant(crabs, p):
    return sum(map(lambda c: abs(c - p), crabs))


def fuel_non_constant(crabs, p):
    return sum(map(lambda c: abs(c - p) * (abs(c - p) + 1) // 2, crabs))


def main():
    with open('input.txt') as f:
        crabs = list(map(int, f.read().split(',')))

    positions1, positions2 = [], []

    for c in range(min(crabs), max(crabs)):
        positions1.append((c, fuel_constant(crabs, c)))
        positions2.append((c, fuel_non_constant(crabs, c)))

    optimum1 = min(positions1, key=lambda p: p[1])
    optimum2 = min(positions2, key=lambda p: p[1])

    print(f'Least fuel comsumed (1): { optimum1[1] }')
    print(f'Least fuel comsumed (2): { optimum2[1] }')


if __name__ == '__main__':
    main()
