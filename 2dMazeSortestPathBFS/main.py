import queue

maze = [[" ", "#", "#", "#", "#", "#", "#"],
        [" ", " ", " ", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", " ", " ", "#"],
        ["#", " ", "#", "#", "#", " ", "#"],
        ["#", " ", " ", " ", "#", " ", "#"],
        ["#", "#", "#", "#", "#", " ", " "]]

q = queue.Queue()
q.put("")
current_move = ""


def get_row_col_position(moves):
    row_position = 0
    column_position = 0

    for move in moves:
        if move == 'L':
            column_position -= 1
        elif move == 'R':
            column_position += 1
        elif move == 'U':
            row_position -= 1
        elif move == 'D':
            row_position += 1

    return row_position, column_position


def is_valid(moves):
    row_position, column_position = get_row_col_position(moves)

    if not (0 <= row_position < len(maze[0]) and 0 <= column_position < len(maze)):
        return False
    elif maze[row_position][column_position] == '#':
        return False
    return True


def is_end(moves):
    end_node_row_pos = len(maze) - 1
    end_node_col_pos = len(maze[0]) - 1
    row_position, column_position = get_row_col_position(moves)

    if row_position == end_node_row_pos and column_position == end_node_col_pos:
        print(f'End reached with moves: {moves}')
        return True
    return False


while not is_end(current_move):
    current_move = q.get()
    for next_move in ['L', 'R', 'U', 'D']:
        moves = current_move + next_move
        if is_valid(moves):
            print(f'valid move adding to q: {moves}')
            q.put(moves)
