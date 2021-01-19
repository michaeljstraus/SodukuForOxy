from random import choice
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
        line = []
        temp = list(input("Enter sudoku line: ").split(", "))
        if len(temp) != 9:
            print("Wrong length. Please try again.")
            temp.clear()
            line = self._getLine()
        for i in temp:
            try:
                line.append(int(i))
            except ValueError:
                line.append('null')

        return line

    def _fillLine(self, line):
        GLf = False
        nullcount = 0
        notInL = []
        itierationCount = 1
        for i in line:
            if i == 'null':
                nullcount += 1

        if nullcount > 0: nullcount -= 1
        stopFlag = False
        h = list(line)
        if len(line) != 9:
            print("Length is wrong. Please try again.")
            stopFlag = True
        elif (len(set(line)) + nullcount) != 9:
            print("Duplicate Number. Please try again.")
            stopFlag = True
        u = 0
        for i in range(1, 10):
            if i not in line:
                notInL.append(i)

        while not GLf and not stopFlag:
            while u < 9:
                if type(line[u]) != type(u):
                    # print("#", u + 1, "is a string")
                    line.remove(line[u])
                    z = choice(notInL)
                    notInL.remove(z)
                    # print(z)
                    line.insert(u, z)
                    u += 1
                elif u < len(line):
                    u += 1
            GLf = self._checkLine(line)
            if GLf == True:
                pass
                # print(l)
            if GLf == False:
                # print(l)
                line = list(h)
                u = 0
                itierationCount += 1

        return line

    def _checkGroups(self, group):
        for lst in group:
            GLf = self._checkLine(lst)
            if not GLf:
                return False
        return True

    def _getGroupRow(self):
        return self.sudoku

    def _getGroupColumn(self):
        n = []
        columnNo = 0
        finalColumns = []
        while columnNo <= 8:
            for value in range(0, 9):
                for line in range(0, 9):
                    if value == columnNo:
                        n.append(self.sudoku[line][value])
            finalColumns.append(list(n))
            n.clear()
            columnNo += 1

        return finalColumns

    def _getGroupBox(self):
        n = []
        finalBoxes = []
        line = 0
        lineStart = 0
        while line < 9:
            for value in range(lineStart, lineStart + 3):
                n.append(self.sudoku[line][value])
            for value in range(lineStart, lineStart + 3):
                n.append(self.sudoku[line + 1][value])
            for value in range(lineStart, lineStart + 3):
                n.append(self.sudoku[line + 2][value])
            if lineStart < 6:
                lineStart += 3
            else:
                lineStart = 0
                line += 3
            finalBoxes.append(list(n))
            n.clear()
        return finalBoxes

    def checkSudoku(self):
        for line in self._getGroupRow():
            if not self._checkLine(line):
                print('rows are bad')
                return False
        for line in self._getGroupColumn():
            if not self._checkLine(line):
                print('columns are bad')
                return False
        for line in self._getGroupBox():
            if not self._checkLine(line):
                print('boxes are bad')
                return False
        print("Good Sudoku")
        return True

    def getSudoku(self): #same as sudoku input
        self.sudoku.clear()
        for i in range(1, 10):
            z = self._getLine()
            self.sudoku.append(z)


    # 1, 2, 3, 4, 5, 6, 7, 8, 9

    def fillSudoku(self):
        lineCount = 0
        n = []
        GSf = False
        itierationCount = 0
        while not GSf:
            for line in self.sudoku:
                n = list(self._fillLine(list(line)))
                self.sudoku.remove(line)
                self.sudoku.insert(lineCount, n)
                lineCount+=1
            print(self.sudoku)
            GSf = self.checkSudoku()
            itierationCount += 1
            lineCount = 0

        # display(filledSudoku)
        print("Number of Itierations:", itierationCount)
        # return itierationCount

    def displaySudoku(self):
        pass




if __name__ == '__main__':
    sudoku = Sudoku()
    # print(sudoku._checkLine([1, 2, 3, 4, 5, 6, 8, 7, 9]))
    print(sudoku._fillLine(['null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null']))
    # # print(sudoku._getLine())
    # sudoku.sudoku = [[8, 2, 7, 1, 5, 4, 3, 9, 6], [9, 6, 5, 3, 2, 7, 1, 4, 8], [3, 4, 1, 6, 8, 9, 7, 5, 2], [5, 9, 3, 4, 6, 8, 2, 7, 1],
    #  [4, 7, 2, 5, 1, 3, 6, 8, 9], [6, 1, 8, 9, 7, 2, 4, 3, 5], [7, 8, 6, 2, 3, 5, 9, 1, 4], [1, 5, 4, 7, 9, 6, 8, 2, 3],
    #  [2, 3, 9, 8, 4, 1, 5, 6, 7]]
    # sudoku.sudoku = [['null', 'null', 'null', 'null', 5, 4, 3, 9, 6], [9, 6, 5, 3, 2, 7, 1, 4, 8], [3, 4, 1, 6, 8, 9, 7, 5, 2], [5, 9, 3, 4, 6, 8, 2, 7, 1],
    #  [4, 7, 2, 5, 1, 3, 6, 8, 9], [6, 1, 8, 9, 7, 2, 4, 3, 5], [7, 8, 6, 2, 3, 5, 9, 1, 4], [1, 5, 4, 7, 9, 6, 8, 2, 3],
    #  [2, 3, 9, 8, 4, 1, 5, 6, 7]]
    # print(sudoku._getGroupColumn())
    # print(sudoku._getGroupRow())
    # print(sudoku._getGroupBox())
    # print(sudoku.checkSudoku())
    # sudoku.getSudoku()
    # print(sudoku.sudoku)
    # sudoku.fillSudoku()

