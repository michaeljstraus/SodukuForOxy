from linechecker import checkLine
from lineinput import getLine
from random import randint
from findgroups import findGroupBox, findGroupColumn, findGroupRow

def fillLine(l):
    GLf=False
    stopFlag = False
    h = list(l)
    if len(l) != 9:
        print("Length is wrong. Please try again.")
        stopFlag = True
    elif len(set(l)) != 9:
        print("Duplicate Number. Please try again.")
        stopFlag = True
    u = 0
    
    while GLf == False and stopFlag == False:
        while u < 9:
            if type(l[u]) != type(u):
                print("#", u+1, "is a string")
                l.remove(l[u])
                z = randint(1,9)
                print(z)
                l.insert(u, z)
                u+=1
            elif u < len(l): u+=1
        GLf = checkLine(l)
        if GLf == True:print(l)
        if GLf == False:
            print(l)
            l = list(h)
            u = 0
    return l
r = []
b=0
n = []
GLf = True
d = ['a', 2, 7, 1, 5, 4, 3, 9, 6, 9, 6, 5, 3, 2, 7, 1, 4, 8, 3, 4, 1, 6, 8, 9, 7, 5, 2, 5, 9, 3, 4, 6, 8, 2, 7, 1, 4, 7, 2, 5, 1, 3, 6, 8, 9, 6, 1, 8, 9, 7, 2, 4, 3, 5, 7, 8, 6, 2, 3, 5, 9, 1, 4, 1, 5, 4, 7, 9, 6, 8, 2, 3, 2, 3, 9, 8, 4, 1, 5, 6, 7]
solved = [8, 2, 7, 1, 5, 4, 3, 9, 6, 9, 6, 5, 3, 2, 7, 1, 4, 8, 3, 4, 1, 6, 8, 9, 7, 5, 2, 5, 9, 3, 4, 6, 8, 2, 7, 1, 4, 7, 2, 5, 1, 3, 6, 8, 9, 6, 1, 8, 9, 7, 2, 4, 3, 5, 7, 8, 6, 2, 3, 5, 9, 1, 4, 1, 5, 4, 7, 9, 6, 8, 2, 3, 2, 3, 9, 8, 4, 1, 5, 6, 7] 
while b < len(d):
    for i in range(b, b+9):
        n.append(d[i])
    b+=9
    n = fillLine(n)
    for i in range(0,9):
        r.append(n[i])
    n.clear()
GLf = findGroupBox(r, GLf, 0)
GLf = findGroupRow(r, GLf, 0)
GLf = findGroupColumn(r, GLf, 0)
print(GLf)

    
#g = [1,2,3,'b',5,6,'s','x',9]
#g = getLine()
#print(type(g[0]))
#g = getLine()
#fillLine(g)
