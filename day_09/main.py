from functools import reduce


def bfs(root, points):
    queue = [root]
    visited_states = {root}
    basin_size = 1

    while len(queue) > 0:
        i, j = queue[0]
        queue = queue[1:]

        ps = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        for n in ps:
            if n not in visited_states and points[n[1]][n[0]] != 9:
                basin_size += 1
                queue.append(n)
                visited_states.add(n)

    return basin_size


def main():
    points = [[9]]

    with open('input.txt') as f:
        for line in f.readlines():
            points.append([9] + list(map(int, list(line.strip()))) + [9])

    points[0] = [9] * len(points[1])
    points.append(points[0])

    size = (len(points[0]), len(points))

    low_points, basin_sizes = [], []

    for j in range(1, size[1] - 1):
        for i in range(1, size[0] - 1):
            ps = [points[j - 1][i], points[j + 1][i],
                  points[j][i - 1], points[j][i + 1]]

            if all(map(lambda p, i=i, j=j: points[j][i] < p, ps)):
                low_points.append(points[j][i])
                basin_sizes.append(bfs((i, j), points))

    basin_sizes.sort()
    basins_prod = reduce(lambda x, y: x * y, basin_sizes[-3:], 1)

    print(f'Risk of low points (1): { sum(low_points) + len(low_points) }')
    print(f'Product of three largest basins (2): { basins_prod }')


if __name__ == '__main__':
    main()
