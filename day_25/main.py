def step(sea):
    new_sea = []

    for i in range(len(sea)):
        row = sea[i]
        new_sea.append(['x'] * len(row))

        j = 0

        while j < len(row):
            if row[j] == '>' and row[(j + 1) % len(row)] == '.':
                new_sea[i][j] = '.'
                new_sea[i][(j + 1) % len(row)] = '>'
                j += 1
            else:
                new_sea[i][j] = row[j]

            j += 1

    sea = new_sea.copy()
    new_sea = [['x'] * len(sea[0]) for _ in range(len(sea))]

    for i in range(len(sea)):
        row = sea[i]

        j = 0

        while j < len(row):
            if row[j] == 'v' and sea[(i + 1) % len(sea)][j] == '.':
                new_sea[i][j] = '.'
                new_sea[(i + 1) % len(sea)][j] = 'v'
            elif new_sea[i][j] == 'x':
                new_sea[i][j] = row[j]

            j += 1

    return new_sea


def print_sea(sea):
    return '\n'.join(map(lambda r: ''.join(r), sea))


def main():
    with open('input.txt') as f:
        sea = list(map(lambda r: list(r.strip()), f.readlines()))

    prev_sea = ''
    steps = 0

    while prev_sea != print_sea(sea):
        prev_sea = print_sea(sea)
        sea = step(sea)
        steps += 1

    print(f'Steps to finish (1): {steps}')


if __name__ == '__main__':
    main()
