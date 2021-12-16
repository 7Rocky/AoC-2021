import math


def get_adjacent(position, risks):
    return map(lambda v: risks.get(position + v, math.inf), [1, -1, 1j, -1j])


def dijkstra(risks, costs):
    previous_costs = {}

    while sum(previous_costs.values()) != sum(costs.values()) \
            or sum(costs.values()) == math.inf:

        previous_costs = costs.copy()

        for position, risk in risks.items():
            if position == 0j:
                continue

            adjacent = get_adjacent(position, costs)
            candidate = risk + min(adjacent)
            cost = costs[position]

            costs[position] = candidate if candidate < cost else cost


def main():
    risks, costs = {}, {}
    pos = 0j

    with open('input.txt') as f:
        for line in f.read().splitlines():
            for i, r in enumerate(line):
                risks[pos + i] = int(r)
                costs[pos + i] = math.inf

            pos += 1j

    length = pos.imag
    last_position = (length - 1) * (1 + 1j)
    costs[0j] = 0

    dijkstra(risks, costs)
    print(f'Minimum cost on one cave (1): {costs[last_position]}')

    new_risks, costs = {}, {}

    for position, risk in risks.items():
        for i in range(5):
            for j in range(5):
                new_risk = risk + i + j - 9 * int(risk + i + j > 9)
                new_risks[position + length * (i + j * 1j)] = new_risk
                costs[position + length * (i + j * 1j)] = math.inf

    last_position = (5 * length - 1) * (1 + 1j)
    costs[0j] = 0

    dijkstra(new_risks, costs)
    print(f'Minimum cost on whole cave (2): {costs[last_position]}')


if __name__ == '__main__':
    main()
