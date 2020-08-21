# create a 9x9 matrix --> containing 3 x (3x3 matrices)
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


# lay out the game
def print_sudoku_board(bo):
    for i in range(len(bo)):  # horizontal
        if i % 3 == 0 and i != 0:  # after every 3 rows print line for visibility purposes
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")  # when reaching the end, draw the next position to the next line

            if j == 8:  # if we are at last position
                print(bo[i][j])  # back slash and go back to the next line
            else:
                print(str(bo[i][j]) + " ", end="")


print_sudoku_board(board)


# choose an empty square
# given this game in a 2D array form, it needs to pick an empty square
def find_empty_square(bo):
    for i in range(len(bo)): #
        for j in range(len(bo[0])): # the length of each row
            if bo[i][j] == 0: # check if that position is 0
                return i, j  # row, col
    return None
# try all #1-9  --> needs a for loop for a constant checker

# find one that passes/valid

# locate next empty square and repeat same steps above

# if doesn't pass then backtrack  --> need to reset that location to 0 if backtracking
