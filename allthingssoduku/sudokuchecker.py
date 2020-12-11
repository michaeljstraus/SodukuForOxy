from sodukuinput import *
from linechecker import *
from lineinput import getLine
from checkgroup import *
def checkSoduku(o):
    GSf = True
    GSf = checkGroupColumn(o, GSf, 0)
    GSf = checkGroupRow(o, GSf, 0)
    GSf = checkGroupBox(o, GSf, 0)
    
    return GSf
if __name__ == '__main__':
    GSf = True
    GSf = checkSoduku(d)
    print(GSf)
    n = []
    goodSodukuFlag = True
    b=0
    d=9
    if len(o) != 81: print("Wrong quantity of numbers. Please try again")
    while goodSodukuFlag == True and b<len(o):
        for i in range(b,d):
            n.append(o[i])        
        goodSodukuFlag = checkLine(n)
        b+=9
        d+=9
        n.clear()

    if b == len(o):
        print("Good Soduku")
        goodSodukuFlag = True 
    elif goodSodukuFlag == False:
        print("Bad Line. Please Reenter Soduku")
        o.clear()
        goodSodukuFlag = False
        
  
checkSoduku([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6, 7, 8, 9])
 