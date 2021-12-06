from collections import Counter


def main():
    with open('input.txt') as f:
        timers = map(int, f.read().split(','))

    counter = {k: 0 for k in range(9)}
    counter.update(dict(Counter(timers)))

    for d in range(256):
        if d == 80:
            print(f'Lanternfish after 80 days (1): { sum(counter.values()) }')

        new_fish = counter[0]

        for i in range(8):
            counter[i] = counter[i + 1]

        counter[6] += new_fish
        counter[8] = new_fish

    print(f'Lanternfish after 256 days (2): { sum(counter.values()) }')


if __name__ == '__main__':
    main()
