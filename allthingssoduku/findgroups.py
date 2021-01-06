from linechecker import checkLine
from linefiller import fillLine
from sodukuinput import display



def findGroupRow(sudoku):
    return sudoku


def findGroupColumn(sudoku):
    n = []
    columnNo = 0
    finalColumns = []
    while columnNo <= 8:
        for value in range(0,9):
            for line in range(0,9):
                if value == columnNo:
                    n.append(sudoku[line][value])
        finalColumns.append(list(n))
        n.clear()
        columnNo+=1

    return finalColumns


def findGroupBox(sudoku):
    n = []
    finalBoxes = []
    line = 0
    lineStart = 0
    while line < 9:
        for value in range(lineStart, lineStart + 3):
            n.append(sudoku[line][value])
        for value in range(lineStart, lineStart + 3):
            n.append(sudoku[line+1][value])
        for value in range(lineStart, lineStart + 3):
            n.append(sudoku[line+2][value])
        if lineStart < 6:lineStart+=3
        else:
            lineStart = 0
            line+=3
        finalBoxes.append(list(n))
        n.clear()
    return finalBoxes


if __name__ == '__main__':
    GSf = True
    d = [8, 2, 7, 1, 5, 4, 3, 9, 6, 9, 6, 5, 3, 2, 7, 1, 4, 8, 3, 4, 1, 6, 8, 9, 7, 5, 2, 5, 9, 3, 4, 6, 8, 2, 7, 1, 4,
         7, 2, 5, 1, 3, 6, 8, 9, 6, 1, 8, 9, 7, 2, 4, 3, 5, 7, 8, 6, 2, 3, 5, 9, 1, 4, 1, 5, 4, 7, 9, 6, 8, 2, 3, 2, 3,
         9, 8, 4, 1, 5, 6, 7]
    d = [[8, 2, 7, 1, 5, 4, 3, 9, 6], [9, 6, 5, 3, 2, 7, 1, 4, 8], [3, 4, 1, 6, 8, 9, 7, 5, 2], [5, 9, 3, 4, 6, 8, 2, 7, 1],
     [4, 7, 2, 5, 1, 3, 6, 8, 9], [6, 1, 8, 9, 7, 2, 4, 3, 5], [7, 8, 6, 2, 3, 5, 9, 1, 4], [1, 5, 4, 7, 9, 6, 8, 2, 3],
     [2, 3, 9, 8, 4, 1, 5, 6, 7]]
    print(findGroupRow(d))
    print(findGroupColumn(d))
    print(findGroupBox(d))
