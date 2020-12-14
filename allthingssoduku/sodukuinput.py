from linechecker import *
from lineinput import *

def inputSoduku():
    d = []
    for i in range(1,10):
        z = getLine()
        for q in range(0,9):
            d.append(z[q])
    return d
# 1 2 3 4 5 6 7 8 9

def display(y):
    t = 0
    while (t <len(y)):
        print(y[t], end = " ")
        if (t + 1) % 9 == 0:
            print(" ")
        t+=1
if __name__ == '__main__':
    w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9]
    display(w)


