import csv
from lib_sudoku_check import *
from lib_sudoku_solver import *

dataset = "./595_1134_bundle_archive/sudoku.csv"


sudoku = [[]]


def read_dataset(_file):
    with open(_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lines = 10
        temp_sudoku_list = []
        for row in csv_reader:
            if lines == 0:
                break
            else:
                temp_sudoku_list.append(row)
                lines -= 1

        return temp_sudoku_list


# sudoku_list = read_dataset(dataset)
sudoku_list = [[
    '003800510008700930100305728000200849801906257000500163964127385382659471010400692']]
# sudoku_list = [[
#     '346179258187023004520640371965832017470916805813750629790261503631485792254397186']]
sudoku = create_sudoku_matrix(sudoku_list[0][0])

for row in sudoku:
    print(row)
    print()

print(check_sudoku(sudoku))

# _solved_sudoku = human_solvable(sudoku)

_solved_sudoku, solvable = bruteforce(sudoku)

for row in _solved_sudoku:
    print(row)
    print()


print(check_sudoku(_solved_sudoku))

# print(sudoku)
