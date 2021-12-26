class Player:
    def __init__(self, id, initial_position, die, score=0):
        self.id = id
        self.position = initial_position
        self.die = die
        self.score = score

    def move_deterministic(self):
        steps = sum(next(self.die) for _ in range(3))
        self.position = (self.position - 1 + steps) % 10 + 1
        self.score += self.position


def deterministic_die():
    n = -1

    while True:
        n += 1
        yield (n % 100) + 1


rf = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]


def wins(p1, p2, t1=21, t2=21):
    if t2 <= 0:
        return 0, 1

    w1, w2 = 0, 0

    for r, f in rf:
        c2, c1 = wins(p2, (p1 + r) % 10, t2, t1 - 1 - (p1 + r) % 10)
        w1, w2 = w1 + f * c1, w2 + f * c2

    return w1, w2


def main():
    with open('input.txt') as f:
        pawns = list(map(int, map(lambda l: l.split()[-1], f.readlines())))

    die = deterministic_die()
    player1 = Player(1, pawns[0], die)
    player2 = Player(2, pawns[1], die)

    turns = 0

    while player2.score < 1000:
        player1.move_deterministic()
        turns += 1

        if player1.score >= 1000:
            final_score = player2.score
            break

        player2.move_deterministic()
        turns += 1
        final_score = player1.score

    print(f'Losing player score times dice (1): {final_score * turns * 3}')
    print(f'Winner universes (2): {max(wins(pawns[0] - 1, pawns[1] - 1))}')


if __name__ == '__main__':
    main()
