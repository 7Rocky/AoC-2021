from collections import defaultdict


def char_range(pairs, template):
    numbers = defaultdict(lambda: 0)
    numbers[template[0]] = 1

    for k, v in pairs.items():
        numbers[k[1]] += v

    values = sorted(numbers.values())
    return values[-1] - values[0]


def main():
    rules = {}
    template = ''

    with open('input.txt') as f:
        template = f.readline().strip()
        f.readline()

        for line in f.readlines():
            pair, element = line.strip().split(' -> ')
            rules[pair] = element

    pairs = defaultdict(lambda: 0)

    for i in range(1, len(template)):
        pair = template[i - 1:i + 1]
        pairs[pair] += 1

    for i in range(40):
        if i == 10:
            print(f'Range on 10 iterations (1): {char_range(pairs, template)}')

        new_pairs = defaultdict(lambda: 0)

        for k, v in pairs.items():
            element = rules[k]
            new_pairs[k[0] + element] += v
            new_pairs[element + k[1]] += v

        pairs = new_pairs

    print(f'Range on 40 iterations (2): {char_range(pairs, template)}')


if __name__ == '__main__':
    main()
