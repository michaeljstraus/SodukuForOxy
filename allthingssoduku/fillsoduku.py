from findgroups import *
from linefiller import fillLine
from sodukuinput import *
from sudokuchecker import *

def fillSoduku(sudoku):
    filledSudoku = []
    n = []
    GSf = False
    while not GSf:
        filledSudoku.clear()
        for line in sudoku:
            n = list(fillLine(list(line)))
            filledSudoku.append(n)
        GSf = checkSudoku(filledSudoku)
    return filledSudoku
if __name__ == '__main__':

    d = [[8, 2, 7, 1, 5, 4, 3, 9, 6], [9, 6, 5, 3, 2, 7, 1, 4, 8], [3, 4, 1, 6, 8, 9, 7, 5, 2], [5, 9, 3, 4, 6, 8, 2, 7, 1],
     [4, 7, 2, 5, 1, 3, 6, 8, 9], [6, 1, 8, 9, 7, 2, 4, 3, 5], [7, 8, 6, 2, 3, 5, 9, 1, 4], [1, 5, 4, 7, 9, 6, 8, 2, 3],
     [2, 3, 9, 8, 4, 1, 5, 6, 7]]
    unfilledSudoku = [[8, 2, 7, 1, 5, 4, 3, 'null', 6], [9, 6, 5, 3, 2, 7, 1, 4, 8], [3, 4, 1, 6, 8, 9, 7, 5, 2], [5, 9, 3, 4, 6, 8, 2, 7, 1],
     [4, 7, 2, 5, 1, 3, 6, 8, 'null'], [6, 1, 8, 'null', 7, 2, 4, 3, 5], [7, 8, 6, 2, 3, 5, 9, 1, 4], [1, 5, 4, 7, 9, 6, 8, 2, 3],
     [2, 3, 9, 8, 4, 1, 5, 6, 7]]
    unfilledSudoku2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null'],['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null'],['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null'],['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null'],['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null'],['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null'],['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null'],['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null']]
    filledSudoku = fillSoduku(unfilledSudoku)
    display(d)
    print(d == filledSudoku)

