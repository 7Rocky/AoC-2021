def match(crit, rep):
    n_bits = len(rep[0])

    for i in range(n_bits):
        if len(rep) == 1:
            break

        bit_sum = sum(int(number[i]) for number in rep)
        match = crit(bit_sum, len(rep) / 2)
        rep = list(filter(lambda s, i=i, m=match: s[i] == m, rep))

    return int(rep[0], 2)


def main():
    with open('input.txt') as f:
        report = list(map(lambda s: s.strip(), f.readlines()))

    n_bits = len(report[0])
    gamma = 0

    for i in range(n_bits):
        bit_sum = sum(int(number[i]) for number in report)
        gamma += 2 ** (n_bits - i - 1) * int(bit_sum > len(report) / 2)

    epsilon = ~gamma & (2 ** n_bits - 1)

    print(f'Power consumption (1): { gamma * epsilon }')

    oxygen = match(lambda n, m: '0' if n < m else '1', report.copy())
    co2 = match(lambda n, m: '1' if n < m else '0', report.copy())

    print(f'Life support (2): { oxygen * co2 }')


if __name__ == '__main__':
    main()
