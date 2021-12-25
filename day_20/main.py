def expand(image, algorithm, odd):
    p = '#' if odd and algorithm[0] == '#' else '.'
    x = len(image[0])
    new_image = [[p] * (x + 4)] * 2

    for line in image:
        new_image.append([p] * 2 + line.copy() + [p] * 2)

    new_image.append([p] * (x + 4))
    new_image.append([p] * (x + 4))

    return new_image


def image_to_num(image):
    stream = ''.join(map(lambda line: ''.join(line), image))
    bits = stream.replace('.', '0').replace('#', '1')

    return int(bits, 2)


def enhance(algorithm, image):
    new_image = []

    for i in range(2, len(image)):
        rows = image[i - 2:i + 1]
        new_image.append([])

        for j in range(2, len(rows[0])):
            sub_image = list(map(lambda r, j=j: r[j - 2:j + 1], rows))
            num = image_to_num(sub_image)
            new_image[i - 2].append(algorithm[num])

    return new_image


def main():
    with open('input.txt') as f:
        algorithm = f.readline().strip()
        f.readline()
        image = list(map(lambda r: list(r.strip()), f.readlines()))

    odd = False

    for i in range(50):
        image = enhance(algorithm, expand(image, algorithm, odd))
        odd = not odd

        if i == 1:
            print(f"Pixels lit (1): {sum(map(lambda r: r.count('#'), image))}")

    print(f"Pixels lit (2): {sum(map(lambda r: r.count('#'), image))}")


if __name__ == '__main__':
    main()
