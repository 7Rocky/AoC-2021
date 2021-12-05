class Board:
    def __init__(self, board):
        self.done = False
        self._board = board
        self._marks = [[0] * 5 for _ in range(5)]

    def round(self, number):
        for i, r in enumerate(self._board):
            for j, c in enumerate(r):
                if c == number:
                    self._marks[i][j] = 1

    def check(self):
        for r in self._marks:
            if sum(r) == 5:
                return self._unmarked()

        for j in range(5):
            if sum(map(lambda r, j=j: r[j], self._marks)) == 5:
                return self._unmarked()

        return -1

    def _unmarked(self):
        res = 0

        for i, r in enumerate(self._marks):
            for j, c in enumerate(r):
                res += self._board[i][j] if c == 0 else 0

        return res


def main():
    boards = []

    with open('input.txt') as f:
        numbers = map(int, f.readline().split(','))

        while f.readline() == '\n':
            b = Board([list(map(int, f.readline().split())) for _ in range(5)])
            boards.append(b)

    results = []

    for number in numbers:
        for b in boards:
            b.round(number)

            if (res := b.check()) != -1 and not b.done:
                results.append(res * number)
                b.done = True

    print(f'First board to win (1): { results[0] }')
    print(f'Last board to win (2): { results[-1] }')


if __name__ == '__main__':
    main()
