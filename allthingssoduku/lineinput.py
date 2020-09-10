from linechecker import checkLine
goodLineFlag = False
def getLine():
    e = []
    d = list(input("Enter sudoku line: ").split(", "))
    print(d)
    for i in d:
        try:e.append(int(i))
        except ValueError:e.append(i)
    return e
"""while goodLineFlag == False:
    c = getLine(1)
    goodLineFlag = checkLine(c)"""  