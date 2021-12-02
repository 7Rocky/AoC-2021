def get_diffs(m):
    diffs = [m[i] - m[i - 1] for i in range(1, len(m))]
    return sum(1 if d > 0 else 0 for d in diffs)


def sliding_window(size, m):
    return [sum(m[i:i+size]) for i in range(0, len(m) - size + 1)]


def main():
    with open('input.txt') as f:
        measurements = list(map(int, f.readlines()))

    print(f'Increasing measurements (1): { get_diffs(measurements) }')

    measurements = sliding_window(3, measurements)
    print(f'Increasing sliding windows (2): { get_diffs(measurements) }')


if __name__ == '__main__':
    main()
