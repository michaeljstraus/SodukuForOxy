from linechecker import checkLine
from linefiller import fillLine
def findGroupRow(s, GSf, q):
    n = []
    b = 0
    while b<len(s) and GSf == True:
        for i in range(b,(b+9)):
            n.append(s[i])
        if q == 0:   
            GSf = checkLine(n)
        if q != 0:
            GSf = fillLine(n)
        b+=9
        n.clear()
    return GSf

def findGroupColumn(s, GSf, q):
    n = []
    p = 0
    while (p < 9) and GSf == True:
        for i in range(0,81):
            if i % 9 == p:
                n.append(s[i])
        if q == 0:
            GSf = checkLine(n)
        if q != 0:
            GSf = fillLine(n)
        n.clear()
        p+=1
    
    return GSf

def findGroupBox(s, GSf, q):
    n = []
    p = 0
    m = 1
    while p < len(s) and GSf == True:
        while m <= 3:
            for i in range(p, p+3):
                n.append(s[i])
                m+=1
        while m <=6 and m > 3:
            for i in range(p+9, p+12):
                n.append(s[i])
                m+=1
        while m > 6 and m <= 9:
            for i in range(p+18, p+21):
                n.append(s[i])
                m+=1
        if q == 0:
            GSf = checkLine(n)
        if q != 0:
            GSf = fillLine(n)
        if p % 9 == 6: p+=21
        else: p+=3
        m = 1
        n.clear()
    return GSf
GSf=True
d = [8, 2, 7, 1, 5, 4, 3, 9, 6, 9, 6, 5, 3, 2, 7, 1, 4, 8, 3, 4, 1, 6, 8, 9, 7, 5, 2, 5, 9, 3, 4, 6, 8, 2, 7, 1, 4, 7, 2, 5, 1, 3, 6, 8, 9, 6, 1, 8, 9, 7, 2, 4, 3, 5, 7, 8, 6, 2, 3, 5, 9, 1, 4, 1, 5, 4, 7, 9, 6, 8, 2, 3, 2, 3, 9, 8, 4, 1, 5, 6, 7]
#findGroupRow(d, GSf, 0)
#findGroupColumn(d, GSf, 0)
findGroupBox(d, GSf, 0)