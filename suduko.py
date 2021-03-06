sudoku =    [[0, 0, 0, 6, 0, 0, 0, 0, 0], 
            [0, 0, 6, 7, 3, 0, 5, 9, 0], 
            [0, 8, 3, 0, 1, 0, 7, 0, 0], 
            [0, 4, 0, 1, 0, 7, 0, 0, 3], 
            [0, 0, 0, 3, 0, 0, 9, 0, 0], 
            [9, 0, 0, 0, 0, 8, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 1], 
            [0, 0, 9, 0, 0, 0, 0, 0, 6], 
            [7, 0, 0, 8, 0, 1, 0, 4, 0]]
def findNextCellToFill(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return x, y
    return -1, -1

def isValid(sudoku, i, j, e):
    rowOk = all([e != sudoku[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != sudoku[x][j] for x in range(9)])
        if columnOk:
            secTopX, secTopY = 3*(i//3), 3*(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if sudoku[x][y] == e:
                        return False
            return True
    return False

def solveSudoku(sudoku, i=0, j=0):
    global backtracks
    i, j = findNextCellToFill(sudoku)
    if i == -1:
        return True

    for e in range(1, 10):
        if isValid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solveSudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False


def printsudoku():
    print("\n\n\n\n\n")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j])+" "
        print(line)
solveSudoku(sudoku)
printsudoku()
