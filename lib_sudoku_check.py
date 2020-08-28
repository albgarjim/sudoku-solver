

def create_sudoku_matrix(_sudoku_string):
    temp_sudoku_matrix = []
    for I in range(0, 9):
        row_string = _sudoku_string[9*I:9*(I+1)]
        row_list = []
        for elem in row_string:
            row_list.append(int(elem))

        temp_sudoku_matrix.append(row_list)

    return temp_sudoku_matrix


def check_rows(_sudoku):
    for row in _sudoku:
        if len(row) == len(set(row)):
            return True
        else:
            return False


def check_columns(_sudoku):
    transposed = list(map(list, zip(*_sudoku)))
    # print(transposed)
    return check_rows(transposed)


def check_single_square(_sudoku, _start_row, _start_col):
    row = []
    for I in range(_start_row, _start_row + 3):
        for K in range(_start_col, _start_col + 3):
            row.append(_sudoku[I][K])

    if len(row) == len(set(row)):
        return True
    else:
        return False


def check_squares(_sudoku):
    if (check_single_square(_sudoku, 0, 0) == False):
        return False
    if (check_single_square(_sudoku, 0, 3) == False):
        return False
    if (check_single_square(_sudoku, 0, 6) == False):
        return False
    if (check_single_square(_sudoku, 3, 0) == False):
        return False
    if (check_single_square(_sudoku, 3, 3) == False):
        return False
    if (check_single_square(_sudoku, 3, 6) == False):
        return False
    if (check_single_square(_sudoku, 6, 0) == False):
        return False
    if (check_single_square(_sudoku, 6, 3) == False):
        return False
    if (check_single_square(_sudoku, 6, 6) == False):
        return False

    return True


def check_sudoku(_sudoku):
    if(check_rows(_sudoku) == False):
        return False
    if(check_columns(_sudoku) == False):
        return False
    if(check_squares(_sudoku) == False):
        return False

    return True


def get_cell_numbers(_sudoku, _row, _col):
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    for I in range(0, len(_sudoku[_row])):
        numbers.discard(_sudoku[_row][I])

    for I in range(3*(int(_row / 3)), 3*(int(_row / 3)) + 3):
        for K in range(3*(int(_col / 3)), 3*(int(_col / 3)) + 3):
            numbers.discard(_sudoku[I][K])

    transposed = list(map(list, zip(*_sudoku)))

    for I in range(0, len(transposed[_col])):
        numbers.discard(transposed[_col][I])

    return list(numbers)
