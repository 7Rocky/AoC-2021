FORWARD, UP, DOWN = 'forward ', 'up ', 'down '


def main():
    with open('input.txt') as f:
        instructions = f.readlines()

    position = 0 + 0j

    for instr in instructions:
        if instr.startswith(FORWARD):
            position += int(instr[len(FORWARD):])
        if instr.startswith(UP):
            position -= int(instr[len(UP):]) * 1j
        if instr.startswith(DOWN):
            position += int(instr[len(DOWN):]) * 1j

    hxd = int(position.real * position.imag)
    print(f'Horizontal position times depth (1): { hxd }')

    position = 0 + 0j
    aim = 0

    for instr in instructions:
        if instr.startswith(FORWARD):
            position += int(instr[len(FORWARD):])
            position += int(instr[len(FORWARD):]) * aim * 1j
        if instr.startswith(UP):
            aim -= int(instr[len(UP):])
        if instr.startswith(DOWN):
            aim += int(instr[len(DOWN):])

    hxd = int(position.real * position.imag)
    print(f'Horizontal position times depth (2): { hxd }')


if __name__ == '__main__':
    main()
