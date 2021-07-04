import numpy as np


ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, column, piece):
    board[row][column] = piece
    
def is_valid_location(board, column):
    return board[ROW_COUNT - 1][column] == 0
    # checks the last row which is the 5th and the column that the player chooses to see if its not occupied
    # There is 6 rows with the top being the last and 7 columns BUT MINUS ONE DUE TO INDEX STARTING AT ZERO


def get_next_open_row(board, column):
    for r in range(ROW_COUNT):  #THIS IS GIVING ME FROM 0 TO ROW COUNT - 1
        if board[r][column] == 0:
            return r  

def print_board(board):
    # Changes the board to start from the bottom up
    print(np.flip(board,0))

def winning_move(board, piece):
    #checking all horizontal locations
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    #checking all vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check for positively sloped diagonals 
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    
    # Check for positively sloped diagonals 
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

board = create_board()
print_board(board)

game_over = False
turn = 0    

while not game_over:
    # ASk for player 1 input
    if turn == 0:
        column = int(input("Player 1 Make your choice (0-6):"))

        if is_valid_location(board,column):
            row = get_next_open_row(board, column)
            drop_piece(board,row,column, 1)

            if winning_move(board,1):
                print("Player 1 wins")
                game_over = True
                break

    # Ask for player 2 input
    else:
        column = int(input("Player 2 Make your choice (0-6):"))

        if is_valid_location(board,column):
            row = get_next_open_row(board, column)
            drop_piece(board,row,column, 2)

            if winning_move(board,2):
               print("Player 2 wins")
               game_over = True
               break

    print_board(board)
    turn += 1
    turn = turn % 2
