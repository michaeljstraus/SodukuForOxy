from linechecker import *
from lineinput import *

def inputSoduku():
    d = []
    for i in range(1,10):
        z = getLine()
        d.append(z)
    return d
# 1 2 3 4 5 6 7 8 9

def display(sudoku):
    for line in range(9):
        for value in range(9):
            if value % 3 == 0 and value != 0: print("| ", end='')
            else:print(end=' ')
            if sudoku[line][value] == 'null':
                print(end='  ')
            else: print(sudoku[line][value], end=' ')
        if line % 3 == 2 and line != 8:
            print()
            print("─"*29, end='')

        print('\r')
    print('\n'*3)
if __name__ == '__main__':
    #w = inputSoduku()
    d = [[8, 2, 7, 1, 5, 4, 3, 'null', 6], [9, 6, 5, 3, 2, 7, 1, 4, 8], [3, 4, 1, 6, 8, 9, 7, 5, 2],
         [5, 9, 3, 4, 6, 8, 2, 7, 1],
         [4, 7, 2, 5, 1, 3, 6, 8, 9], [6, 1, 8, 9, 7, 2, 4, 3, 5], [7, 8, 6, 2, 3, 5, 9, 1, 4],
         [1, 5, 4, 7, 9, 6, 8, 2, 3],
         [2, 3, 9, 8, 4, 1, 5, 6, 7]]
    display(d)
#   1, x, x, x, x, x, x, x, x

