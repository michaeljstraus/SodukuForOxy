from linechecker import checkLine
goodLineFlag = False
def getLine():
    e = []
    d = list(input("Enter sudoku line: ").split(", "))
    for i in d:
        try:
            e.append(int(i))
        except ValueError:
            e.append('null')
            
    print(e)
    return e
"""while goodLineFlag == False:
    c = getLine(1)
    goodLineFlag = checkLine(c)"""  