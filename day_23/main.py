ROOMS = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
ROOM_POSITIONS = set(ROOMS.values())
MOVE_COSTS = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def can_reach(board, start_pos, end_pos):
    a = min(start_pos, end_pos)
    b = max(start_pos, end_pos)

    for pos in range(a, b + 1):
        if pos == start_pos:
            continue
        if pos in ROOM_POSITIONS:
            continue
        if board[pos] != '.':
            return False

    return True


def room_only_contains_goal(board, piece, dest_pos):
    in_room = board[dest_pos]
    return len(in_room) == in_room.count('.') + in_room.count(piece)


def get_piece_from_room(room):
    for c in room:
        if c != '.':
            return c


def possible_moves(board, pos):
    piece = board[pos]

    if pos not in ROOM_POSITIONS:
        if can_reach(board, pos, ROOMS[piece]) and room_only_contains_goal(board, piece, ROOMS[piece]):
            return [ROOMS[piece]]

        return []

    moving_letter = get_piece_from_room(piece)

    if pos == ROOMS[moving_letter] and room_only_contains_goal(board, moving_letter, pos):
        return []

    possible = []

    for dest in range(len(board)):
        if dest == pos:
            continue
        if dest in ROOM_POSITIONS and ROOMS[moving_letter] != dest:
            continue
        if ROOMS[moving_letter] == dest:
            if not room_only_contains_goal(board, moving_letter, dest):
                continue
        if can_reach(board, pos, dest):
            possible.append(dest)

    return possible


def add_to_room(letter, room):
    room = list(room)
    dist = room.count('.')
    room[dist - 1] = letter
    return ''.join(room), dist


def move(board, pos, dest):
    new_board = board.copy()
    dist = 0
    moving_letter = get_piece_from_room(board[pos])

    if len(board[pos]) == 1:
        new_board[pos] = '.'
    else:
        new_room = ''
        found = False

        for c in board[pos]:
            if c == '.':
                dist += 1
                new_room += c
            elif not found:
                new_room += '.'
                dist += 1
                found = True
            else:
                new_room += c

        new_board[pos] = new_room

    dist += abs(pos - dest)

    if len(board[dest]) == 1:
        new_board[dest] = moving_letter
        return new_board, dist * MOVE_COSTS[moving_letter]

    new_board[dest], addl_dist = add_to_room(moving_letter, board[dest])
    dist += addl_dist
    return new_board, dist * MOVE_COSTS[moving_letter]


def solve(board):
    states = {tuple(board): 0}
    queue = [board]

    while queue:
        board = queue.pop()

        for pos, piece in enumerate(board):
            if get_piece_from_room(piece) is None:
                continue

            dests = possible_moves(board, pos)

            for dest in dests:
                new_board, addl_cost = move(board, pos, dest)
                new_cost = states[tuple(board)] + addl_cost
                new_board_tuple = tuple(new_board)
                cost = states.get(new_board_tuple)
                if cost is None or new_cost < cost:
                    states[new_board_tuple] = new_cost
                    queue.append(new_board)

    return states


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    u = list(lines[2].strip().replace('#', ''))
    d = list(lines[3].strip().replace('#', ''))

    board = [
        '.',
        '.',
        u[0] + d[0],
        '.',
        u[1] + d[1],
        '.',
        u[2] + d[2],
        '.',
        u[3] + d[3],
        '.',
        '.'
    ]

    states = solve(board)
    target = ('.', '.', 'AA', '.', 'BB', '.', 'CC', '.', 'DD', '.', '.')
    print('Least energy required (1):', states[target])

    board = [
        '.',
        '.',
        u[0] + 'DD' + d[0],
        '.',
        u[1] + 'CB' + d[1],
        '.',
        u[2] + 'BA' + d[2],
        '.',
        u[3] + 'AC' + d[3],
        '.',
        '.'
    ]

    states = solve(board)
    target = ('.', '.', 'AAAA', '.', 'BBBB', '.', 'CCCC', '.', 'DDDD', '.', '.')
    print('Least energy required (2):', states[target])


if __name__ == '__main__':
    main()
