from collections import Counter
from functools import reduce


MATCHES = {'(': ')', '[': ']', '{': '}', '<': '>'}
SCORES = {'(': 1, '[': 2,  '{': 3,    '<': 4,
          ')': 3, ']': 57, '}': 1197, '>': 25137}


def syntax_checker_score(counter):
    return sum(SCORES[k] * v for k, v in counter.items())


def autocomplete_score(completions):
    scores = sorted(reduce(lambda t, c: t * 5 + SCORES[c], list(completion), 0)
                    for completion in completions)

    return scores[len(scores) // 2]


def main():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    corrupt, incomplete = [], []

    for line in lines:
        stack = []
        is_corrupt = False

        for c in line:
            if c in '([{<':
                stack.append(c)
            elif c in ')]}>':
                if MATCHES[stack[-1]] == c:
                    stack = stack[:-1]
                else:
                    corrupt.append(c)
                    is_corrupt = True
                    break

        if not is_corrupt and len(stack):
            incomplete.append(''.join(stack)[::-1])

    print(f'Syntax score (1): { syntax_checker_score(Counter(corrupt)) }')
    print(f'Autocomplete score (2): { autocomplete_score(incomplete) }')


if __name__ == '__main__':
    main()
