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

def display_board():   

    print(board[0] + " | " + board[1] + " | " +  board[2])
    print(board[3] + " | " + board[4] + " | " +  board[5])
    print(board[6] + " | " + board[7] + " | " +  board[8])

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


def handle_turn(current_player):
    position=0
    while position in range(0,9):
        position = int(input("Choose a position from 1-9: ")) - 1
        board[position]="X"
        display_board()


def game_over():
    check_win()
    check_tie()

def check_win():
    # check rows
    row_winner = check_rows()
    # check columns 
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()


    return

def check_rows():
    return

def check_columns():
    return

def check_diagonals():
    return

def check_tie():
    return

def flip_player():
    return

play_game()