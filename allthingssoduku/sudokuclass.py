class Sudoku:
    sudoku = []

    def _checkLine(self, line):
        d = list(line)
        d.sort()
        s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if s == d:
            goodLineFlag = True
        else:
            goodLineFlag = False
        return goodLineFlag

    def _getLine(self): #should be same as line input function
        pass

    def _fillLine(self, line):
        pass

    def _checkGroups(self):
        pass

    def _getGroups(self): #same as find groups.py
        pass

    def checkSudoku(self):
        pass

    def getSudoku(self): #same as sudoku input
        pass

    def fillSudoku(self):
        pass

    def displaySudoku(self):
        pass




if __name__ == '__main__':
    sudoku = Sudoku()
    print(sudoku._checkLine([1, 2, 3, 4, 5, 6, 8, 7, 9]))
