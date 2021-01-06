from linechecker import checkLine
from findgroups import findGroupRow, findGroupColumn, findGroupBox


def checkGroup(group):
    for lst in group:
        GLf = checkLine(lst)
        if not GLf: return False
    return True

if __name__ == '__main__':
    o = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1,
         2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2,
         3, 4, 5, 6, 7, 8, 9]
    d = [8, 2, 7, 1, 5, 4, 3, 9, 6, 9, 6, 5, 3, 2, 7, 1, 4, 8, 3, 4, 1, 6, 8, 9, 7, 5, 2, 5, 9, 3, 4, 6, 8, 2, 7, 1, 4,
         7, 2, 5, 1, 3, 6, 8, 9, 6, 1, 8, 9, 7, 2, 4, 3, 5, 7, 8, 6, 2, 3, 5, 9, 1, 4, 1, 5, 4, 7, 9, 6, 8, 2, 3, 2, 3,
         9, 8, 4, 1, 5, 6, 7]
    print(checkGroup(findGroupRow(o, True)))
    print(checkGroup(findGroupColumn(o, True)))
    print(checkGroup(findGroupBox(o, True)))
