from findgroups import findGroupBox, findGroupColumn, findGroupRow
from linefiller import fillLine
from sodukuinput import *

def fillSoduku(soduku):
    realSoduku = []
    b = 0
    n = []
    GSf = False
    while GSf == False:
        while b < 81:
            for i in range(b, b+9):
                n.append(soduku[i])
            fillLine(n)
            for i in range(0,9):
                realSoduku.append(n[i])
            n.clear()
            b+=9
        n.clear()
        GSf = findGroupBox(realSoduku, GSf, 0)
        GSf = findGroupColumn(realSoduku, GSf, 0)
        GSf = findGroupRow(realSoduku, GSf, 0)
        print("Failed Attempt. Trying Again.")
        print(GSf)
        b = 0
        if GSf == False:
            realSoduku.clear()
    return realSoduku
if __name__ == '__main__':
    d = [8, 2, 7, 1, 5, 4, 3, 9, 6, 9, 6, 5, 3, 2, 7, 1, 4, 8, 3, 4, 1, 6, 8, 9, 7, 5, 2, 5, 9, 3, 4, 6, 8, 2, 7, 1, 4, 7, 2, 5, 1, 3, 6, 8, 9, 6, 1, 8, 9, 7, 2, 4, 3, 5, 7, 8, 6, 2, 3, 5, 9, 1, 4, 1, 5, 4, 7, 9, 6, 8, 2, 3, 2, 3, 9, 8, 4, 1, 5, 6, 7]
    realSoduku = fillSoduku(d)
    print(realSoduku)