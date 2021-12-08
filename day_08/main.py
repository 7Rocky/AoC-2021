def match_nine(sample, digits, three):
    for d in sample:
        if len(d) == 6 and all(c in d for c in three):
            digits[d] = 9

    sample.difference_update(digits.keys())


def match_three(sample, digits, seven):
    for d in sample:
        if len(d) == 5 and all(c in d for c in seven):
            digits[d] = 3
            three = d

    sample.difference_update(digits.keys())
    return three


def match_six(sample, digits):
    for d in sample:
        if len(d) == 6:
            digits[d] = 6
            six = d

    sample.difference_update(digits.keys())
    return six


def match_zero(sample, digits, seven):
    for d in sample:
        if len(d) == 6 and all(c in d for c in seven):
            digits[d] = 0

    sample.difference_update(digits.keys())


def match_two_five(sample, digits, six):
    for d in sample:
        digits[d] = 5 if all(c in six for c in d) else 2


def match_one_four_seven_eight(sample, digits):
    for d in sample:
        if len(d) == 2:
            digits[d] = 1
        if len(d) == 3:
            digits[d] = 7
            seven = d
        if len(d) == 4:
            digits[d] = 4
        if len(d) == 7:
            digits[d] = 8

    sample.difference_update(digits.keys())
    return seven


def match_digits(sample):
    digits = {}

    seven = match_one_four_seven_eight(sample, digits)
    three = match_three(sample, digits, seven)
    match_nine(sample, digits, three)
    match_zero(sample, digits, seven)
    six = match_six(sample, digits)
    match_two_five(sample, digits, six)

    return digits


def sort_s(s):
    return ''.join(sorted(list(s)))


def main():
    signal_patterns, output_values = [], []

    with open('input.txt') as f:
        for line in f.readlines():
            signal_pattern, output_value = line.strip().split(' | ')
            signal_patterns.append(set(map(sort_s, signal_pattern.split())))
            output_values.append(list(map(sort_s, output_value.split())))

    numbers, result = 0, 0

    for output_value in output_values:
        numbers += sum(map(lambda d: int(len(d) % 7 < 5), output_value))

    for sample, display in zip(signal_patterns, output_values):
        digits = match_digits(sample)
        result += sum(digits[d] * 10 ** (3 - i) for i, d in enumerate(display))

    print(f'Number of digits 1, 4, 7, 8 (1): { numbers }')
    print(f'Sum of all displays (2): { result }')


if __name__ == '__main__':
    main()
