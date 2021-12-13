def print_points(points, max_x, max_y):
    origami = []

    for y in range(max_y + 1):
        origami.append('\n')

        for x in range(max_x + 1):
            origami.append('#' if (x, y) in points else '.')

    print(''.join(origami))


def main():
    points, folds = set(), []

    with open('input.txt') as f:
        while (line := f.readline().strip()):
            points.add(tuple(map(int, line.split(','))))

        length = len('fold along ')

        for line in f.readlines():
            axis, fold = line[length:length + 1], int(line[length + 2:])
            folds.append((2 * bool(axis == 'x') - 1) * fold)

    for i, fold in enumerate(folds):
        new_points = set()

        for x, y in points:
            x = (2 * fold) - x if fold > 0 and x > fold else x
            y = (-2 * fold) - y if fold < 0 and y > -fold else y
            new_points.add((x, y))

        points = new_points

        if i == 0:
            print(f'Number of points after first fold (1): {len(points)}')

    x, y = map(lambda i: map(lambda p, i=i: p[i], points), [0, 1])

    print('Hidden message (2):', end='')
    print_points(points, max(x), max(y))


if __name__ == '__main__':
    main()
