
#print(s)
#print(type(s))
def checkLine(t):
    d = []
    d = list(t)
    d.sort()
    s = [1,2,3,4,5,6,7,8,9]
    if s == d:
        goodLineFlag = True
        print("Good Line")
    else:
        goodLineFlag = False
        print("Bad Line")
    return goodLineFlag
