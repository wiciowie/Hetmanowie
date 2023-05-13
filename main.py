import sys


def check_row(row):
    count = 2
    for i in range(n):
        if board[i][row] == "Q":
           count = count - 1
    if count == 0:
        sys.exit("Hetman wykryty")


def check_col(col):
    count = 2
    for i in range(n):
        #print(col,i)
        if board[col][i] == "Q":
           count = count - 1
        if count == 0:
            sys.exit("Hetman wykryty")


def check_firstQsquad(row,col):
    count = 2
    for i in range(n):
        # print(col,i)
        if board[row-i][col-i] == "Q":
            count = count - 1
            if count == 0:
                sys.exit("Hetman wykryty")

        if row - i == 0 or col - 1 == 0:
            break
def check_secendQsquad(row,col):
    count = 2
    for i in range(n):
        # print(col,i)
        if board[row-i][col+i] == "Q":
            count = count - 1
            if count == 0:
                sys.exit("Hetman wykryty")

        if row - i == 0 or col + i == 7:
            break
def check_thirdQsquad(row,col):
    count = 2
    for i in range(n):
        # print(col,i)
        if board[row+i][col+i] == "Q":
            count = count - 1
            if count == 0:
                sys.exit("Hetman wykryty")

        if row + i == 7 or col + i == 7:
            break
def check_fourthQsquad(row,col):
    count = 2
    for i in range(n):
        # print(col,i)
        if board[row+i][col-i] == "Q":
            count = count - 1
            if count == 0:
                sys.exit("Hetman wykryty")

        if row + i == 7 or col - i == 0:
            break






board = [
    ["-", "-", "-", "-", "Q", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "Q", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"]]

goodQueanState = True
n = 8

for row in range(n):
    for col in range(n):
       # print(col,row)
        if board[row][col] == "Q":
            print(row, col)
            check_col(col)
            check_row(row)
            check_firstQsquad(row, col)
            check_secendQsquad(row, col)
            check_thirdQsquad(row, col)
            check_fourthQsquad(row, col)
print("JEST GIT")
