from findgroups import findGroupBox, findGroupColumn, findGroupRow
from linefiller import fillLine
from sodukuinput import *
from sodukuinput import display

def fillSoduku(soduku):
    realSoduku = []
    b = 0
    n = []
    goodBoxFlag = False
    goodColumnFlag = False
    goodRowFlag = False
    while (not goodBoxFlag) or (not goodColumnFlag) or (not goodRowFlag):
        while b < 81:
            for i in range(b, b+9):
                n.append(soduku[i])
            fillLine(n)
            for i in range(0,9):
                realSoduku.append(n[i])
            n.clear()
            b+=9
        n.clear()
        goodBoxFlag = findGroupBox(realSoduku, goodBoxFlag, 0)
        goodColumnFlag = findGroupColumn(realSoduku, goodColumnFlag, 0)
        goodRowFlag = findGroupRow(realSoduku, goodRowFlag, 0)
        print("Failed Attempt. Trying Again.")
        b = 0
        if (not goodBoxFlag) or (not goodColumnFlag) or (not goodRowFlag):
            realSoduku.clear()
    return realSoduku
if __name__ == '__main__':
    d = [8, 2, 7, 1, 5, 4, 3, 9, 6, 9, 6, 5, 3, 2, 7, 1, 4, 8, 3, 4, 1, 6, 8, 9, 7, 5, 2, 5, 9, 3, 4, 6, 8, 2, 7, 1, 4, 7, 2, 5, 1, 3, 6, 8, 9, 6, 1, 8, 9, 7, 2, 4, 3, 5, 7, 8, 6, 2, 3, 5, 9, 1, 4, 1, 5, 4, 7, 9, 6, 8, 2, 3, 2, 3, 9, 8, 4, 1, 5, 6, 7]
    realSoduku = fillSoduku(d)
    print(realSoduku)
    display(d)