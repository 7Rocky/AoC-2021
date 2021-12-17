from functools import reduce


bit_stream = []
bytes_read = 0
sum_of_versions = 0


def get_bits(n):
    global bytes_read
    global bit_stream

    bytes_read += n
    bits = bit_stream[:n]
    bit_stream = bit_stream[n:]

    return bits


def decode_bits(x):
    return int(''.join(x), 2)


def get_literal():
    number = []
    last = False

    while not last:
        last = decode_bits(get_bits(1)) == 0
        number.extend(get_bits(4))

    return decode_bits(number)


def decode_packet():
    global sum_of_versions

    version = decode_bits(get_bits(3))
    type_id = decode_bits(get_bits(3))
    sum_of_versions += version

    if type_id == 4:
        return get_literal()

    length_type_id = decode_bits(get_bits(1))
    values = []

    if length_type_id == 0:
        length = decode_bits(get_bits(15))
        position = bytes_read

        while position + length > bytes_read:
            values.append(decode_packet())
    else:
        n_sub_packets = decode_bits(get_bits(11))

        for _ in range(n_sub_packets):
            values.append(decode_packet())

    match type_id:
        case 0:
            return sum(values)
        case 1:
            return reduce(lambda x, y: x * y, values, 1)
        case 2:
            return min(values)
        case 3:
            return max(values)
        case 5:
            return int(values[0] > values[1])
        case 6:
            return int(values[0] < values[1])
        case 7:
            return int(values[0] == values[1])


def main():
    global bit_stream

    with open('input.txt') as f:
        packet = f.read().strip()

    bit_stream = list(f'{int(packet, 16):0{len(packet) * 4}b}')
    packet_result = decode_packet()

    print(f'Sum of versions (1): {sum_of_versions}')
    print(f'Resulting value (2): {packet_result}')


if __name__ == '__main__':
    main()
