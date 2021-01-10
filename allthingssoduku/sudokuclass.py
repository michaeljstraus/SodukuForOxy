class Sudoku:
    sudoku = []

    def _checkLine(self, line):
        d = list(line)
        d.sort()
        s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if s == d:
            goodLineFlag = True
            # print("Good Line")
        else:
            goodLineFlag = False
            # print("Bad Line")
        return goodLineFlag

    def _inputLine(self):
        pass

    def _fillLine(self, line):
        pass
if __name__ == '__main__':
    sudoku = Sudoku()
    print(sudoku._checkLine([1, 2, 3, 4, 5, 6, 8, 7, 9]))