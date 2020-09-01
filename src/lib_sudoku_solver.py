from lib_sudoku_check import *
import copy

solved = False


def human_solvable(_sudoku):
    count = 0
    while (solved == False and count < 81):
        count += 1
        _sudoku = solve_cells(_sudoku)

    return _sudoku


itr = 0


def bruteforce(_sudoku):
    global itr
    itr += 1
    # if itr % 50 == 0:
    #     for row in _sudoku:
    #         print(row)
    #         print()
    #     print()
    #     print()
    for I in range(0, len(_sudoku)):
        for K in range(0, len(_sudoku[I])):
            if (_sudoku[I][K] == 0):
                candidates = get_cell_numbers(_sudoku, I, K)

                if len(candidates) == 0:
                    return _sudoku, False

                for cand in candidates:
                    _sudoku[I][K] = cand
                    sudoku_copy = copy.deepcopy(_sudoku)
                    _sudoku_copy, res = bruteforce(sudoku_copy)
                    if res == True:
                        return _sudoku_copy, True

                _sudoku[I][K] = 0

                return _sudoku, False

    print(itr)
    return _sudoku, True


def solve_cells(_sudoku):
    global solved

    solved = True
    for I in range(0, len(_sudoku)):
        map_candidates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        list_add = []
        for K in range(0, len(_sudoku[I])):
            if (_sudoku[I][K] == 0):
                solved = False
                candidates = get_cell_numbers(_sudoku, I, K)
                if(len(candidates) == 1):
                    _sudoku[I][K] = candidates[0]
                else:
                    for cand in candidates:
                        map_candidates[cand] += 1

        for M in range(1, len(map_candidates)):
            if map_candidates[M] == 1:
                list_add.append(M)

        for K in range(0, len(_sudoku[I])):
            if (_sudoku[I][K] == 0):
                solved = False
                candidates = get_cell_numbers(_sudoku, I, K)

                for val in list_add:
                    if val in candidates:
                        _sudoku[I][K] = val

    return _sudoku
