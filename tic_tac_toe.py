# board 
# display board
# play game
# handle turn
# check win
    # check row
    # check columns
# check tie
# flip player 
# count wins
# UI 



# ----Global Variables----
# Game board
board=["-","-","-",
    "-","-","-",
    "-","-","-"]

# If game is still on
game_on = True

# Who woin? or tie
winner = None

# Whose turn
current_player ="X"

#-------------

def play_game():

    # Display initial board
    display_board()
    # Takes turns till game is over
    while game_on:
        # Handle turns of an a player
        handle_turn(current_player)

        # Checks if game is over
        game_over()

        # Flip to the other player
        flip_player()
    if winner == "X" or winner =="O":
        print(winner + " Won.")
    else:
        winner == None
        print("Tie")  

def display_board():   

    print(board[0] + " | " + board[1] + " | " +  board[2])
    print(board[3] + " | " + board[4] + " | " +  board[5])
    print(board[6] + " | " + board[7] + " | " +  board[8])


def handle_turn(current_player):
    position=0
    while position in range(0,9):
        position = input("Choose a position from 1-9: ")
        # Get correct index in our board list
        position = int(position) - 1
        board[position] = current_player
        display_board()


def game_over():
    check_win()
    check_tie()

def check_win():
    # set up global variables 
    global winner
    # checking rows
    row_win = check_rows()
    # checking columns 
    column_win = check_columns()
    # checking diagonals
    diagonal_win = check_diagonals()
    if row_win:
        winner = row_win
    elif column_win:
        winner = column_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        #there was a tie
        winner = None


def check_rows():
    # set up global variables
    global game_on
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match then there is a win.
    if row_1 or row_2 or row_3:
        game_on = False
    # return winner (X or O)
    if row_1:
       return board[0]
    elif row_2:
       return board[3]
    elif row_3:
       return board[6]
    
    return

def check_columns():
    # set up global variables
    global game_on
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    # If any columns does have a match then there is a win.
    if col_1 or col_2 or col_3:
        game_on = False
    # return winner (X or O)
    if col_1:
       return board[0]
    elif col_2:
       return board[1]
    elif col_3:
       return board[2]
    return


def check_diagonals():
    # set up global variables
    global game_on
    d_1 = board[0] == board[4] == board[8] != "-"
    d_2 = board[2] == board[4] == board[6] != "-"
    # If any diagonals does have a match then there is a win.
    if d_1 or d_2:
        game_on = False
    # return winner (X or O)
    if d_1:
       return board[0]
    elif d_2:
       return board[2]

    return

def check_tie():
    return

def flip_player():
    # set up global variables
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return




play_game()