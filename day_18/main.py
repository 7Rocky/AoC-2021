from functools import reduce
from itertools import permutations


class Number:
    value = 0
    left, right = None, None

    def __init__(self, element=None, parent=None):
        self.parent = parent

        if type(element) == list:
            self.left = Number(element[0], self)
            self.right = Number(element[1], self)
        elif type(element) == int:
            self.value = element

    def __add__(self, number):
        res = Number()
        res.left = self
        res.right = number
        self.parent = res
        number.parent = res

        while res.reduce():
            continue

        return res

    def magnitude(self):
        if self.left is None and self.right is None:
            return self.value

        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def get_level(self):
        level = 0
        n = self

        while n.parent is not None:
            n = n.parent
            level += 1

        return level

    def reduce(self):
        return self.do_explode() or self.split()

    def do_explode(self):
        if self.left is None and self.right is None:
            if self.get_level() > 4:
                self.parent.explode()
                return True
        else:
            return self.left.do_explode() or self.right.do_explode()

        return False

    def explode(self):
        p = self.parent

        if p.left == self:
            self.explode_left(p)
        elif p.right == self:
            self.explode_right(p)

        self.left, self.right = None, None

    def explode_left(self, p):
        if p.right.left is None:
            p.right.value += self.right.value
        else:
            p.right.left.value += self.right.value

        while p.parent is not None and p.parent.left == p:
            p = p.parent

        if p.parent is not None:
            p = p.parent.left

            while p.right is not None:
                p = p.right

            p.value += self.left.value

    def explode_right(self, p):
        if p.left.right is None:
            p.left.value += self.left.value
        else:
            p.left.right.value += self.left.value

        while p.parent is not None and p.parent.right == p:
            p = p.parent

        if p.parent is not None:
            p = p.parent.right

            while p.left is not None:
                p = p.left

            p.value += self.right.value

    def split(self):
        if self.left is None and self.right is None:
            if self.value > 9:
                self.left = Number(self.value // 2, self)
                self.right = Number((self.value + 1) // 2, self)
                self.value = 0
                return True
        else:
            return self.left.split() or self.right.split()

        return False


def main():
    with open('input.txt') as f:
        lines = f.readlines()
        numbers = [Number(eval(line)) for line in lines]

    print(f'Sum result (1): {reduce(lambda a, b: a + b, numbers).magnitude()}')

    magnitudes = []

    for a, b in permutations(lines, 2):
        magnitudes.append((Number(eval(a)) + Number(eval(b))).magnitude())
        magnitudes.append((Number(eval(a)) + Number(eval(b))).magnitude())

    print(f'Maximum magnitude (2): {max(magnitudes)}')


if __name__ == '__main__':
    main()
