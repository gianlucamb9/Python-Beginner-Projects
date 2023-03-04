import random

#GAME CODE

#Function to print out a board with a list as argument.
#Output: String
def display_board(board):
    print("\n")
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])
    print("\n")

#Function to asign X or O to player
#Output: Tuple
def player_marker():
    marker = input("Choose your marker: ").upper()

    while marker != "X" and marker != "O":
        print("Please select X or O")
    
    if marker == "X":
        print("Player 1 is X. Player 2 is O.", "\n")
        return ("X", "O")
    else:
        print("Player 1 is O. Player 2 is X", "\n")
        return ("O", "X")

#Function to place the marker in a position in the board. It needs to take...
#...the board, the marker to place, and the desired position in the board.
#Output: None
def place_marker(board,marker,position):
    board[position] = marker


#Function to check if a mark has won. Takes the played board and the mark to check for.
#Output: Bool
def win_check(board, mark):
    return ((board[0]==board[1]==board[2]==mark or 
             board[3]==board[4]==board[5]==mark or 
             board[6]==board[7]==board[8]==mark or 
             board[0]==board[3]==board[6]==mark or 
             board[1]==board[4]==board[7]==mark or 
             board[2]==board[5]==board[8]==mark or 
             board[0]==board[4]==board[8]==mark or 
             board[6]==board[4]==board[2]==mark))

#Function to decide which player goes first.
#Output: String
def coin_flip():

    while True:
        coin_choice = input("Heads or Tails? ").title()

        if coin_choice == "Heads":
            break
        elif coin_choice == "Tails":
            break
        else:
            print("Please chose Heads or Tails.")
            continue

    coin_options = ["Heads", "Tails"]
    coin_toss = random.choice(coin_options)
    print(f"It is {coin_toss}")

    if coin_choice == coin_toss:
        print("Player 1 goes first.", "\n")
        return "Player 1"
    else:
        print("Player 2 goes first.", "\n")
        return "Player 2"

#Function to check if selected position is free in the board.
#Output: Bool
def check_space(board, position):
    return (board[position]).isdigit()

#Function to check if board is full.
#Output: Bool
def full_board(board):
    for x in board:
        if x in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
            return False
    return True

#Function to get players next position. If it is free, returns the position.
#Output: Int
def next_position(board):
    position = int(input("Choose your next position: "))

    while True:
        if position in [0,1,2,3,4,5,6,7,8] and check_space(board,position):
            return position
        else:
            position = int(input("Please choose another position: "))
                           
#Function to replay:
def play_again():
    replay = input("Do you want to play again? ").lower()

    while replay != "yes" and replay != "no":
        replay = input("Please enter Yes or No: ")
    
    if replay == "yes":
        return True
    else:
        return False
    

#GAME SCRIPT

print("\n")
print("Welcome to Tic-Tac-Toe!")

while True:

    playing_board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    p1marker,p2marker = player_marker()
    turn = coin_flip()

    while True:
        ready2play = input("Are you ready to play? ").lower()
        if ready2play != "yes" and ready2play != "no":
            print("Please enter Yes or No.")
            continue
        elif ready2play == "yes":
            print("Let's go!")
            game_on = True
            break
        elif ready2play == "no":
            print("Come back soon!", "\n")
            game_on = False
            break
    
    while game_on:
        if turn == "Player 1":
            display_board(playing_board)
            position = next_position(playing_board)
            place_marker(playing_board,p1marker,position)

            if win_check(playing_board,p1marker):
                display_board(playing_board)
                print("Player 1 Wins!")
                game_on = False
            else:
                if full_board(playing_board):
                    display_board(playing_board)
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = "Player 2"
        
        else:
            display_board(playing_board)
            position = next_position(playing_board)
            place_marker(playing_board,p2marker,position)

            if win_check(playing_board,p2marker):
                display_board(playing_board)
                print("Player 2 Wins!")
                game_on = False
            else:
                if full_board(playing_board):
                    display_board(playing_board)
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = "Player 1"

    if play_again():
        print("Awesome. Setting up new game...", "\n")
    else:
        print("Thanks for playing!", "\n")
        break
