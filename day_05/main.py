def cover(start, end):
    x1, y1 = map(int, start.split(','))
    x2, y2 = map(int, end.split(','))

    if x1 != x2 and y1 != y2:
        return []

    points = [start, end]

    if x1 == x2:
        incr = 1 if y1 < y2 else -1

        for y in range(y1 + incr, y2, incr):
            points.append(f'{x1},{y}')

    if y1 == y2:
        incr = 1 if x1 < x2 else -1

        for x in range(x1 + incr, x2, incr):
            points.append(f'{x},{y1}')

    return points


def cover_diagonals(start, end):
    x1, y1 = map(int, start.split(','))
    x2, y2 = map(int, end.split(','))

    if abs(x1 - x2) != abs(y1 - y2):
        return []

    points = [start, end]

    incr_x = 1 if x1 < x2 else -1
    incr_y = 1 if y1 < y2 else -1

    for i in range(1, abs(x1 - x2)):
        points.append(f'{x1 + incr_x * i},{y1 + incr_y * i}')

    return points


def get_repeated_points(lines, diagonals=False):
    points, repeated_points = set(), set()

    for line in lines:
        start, end = line.split(' -> ')
        points_in_lines = cover(start, end)

        if diagonals:
            points_in_lines += cover_diagonals(start, end)

        for p in points_in_lines:
            length = len(points)
            points.add(p)

            if length == len(points):
                repeated_points.add(p)

    return len(repeated_points)


def main():
    with open('input.txt') as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))

    print(f'Overlapping lines (1): { get_repeated_points(lines) }')
    print(f'Overlapping lines (2): { get_repeated_points(lines, True) }')


if __name__ == '__main__':
    main()
