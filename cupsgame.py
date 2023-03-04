from random import shuffle

#GAME CODE

#Ask player if he's ready to play
def ready():
    
    ready = input("Are you ready to play? Y or N: ")
    
    while ready.lower() not in ("y", "n"):
        ready = input("Please only Y or N: ")
        
    return ready

#Shuffle the cups
def shuffle_cups(cups):
    shuffle(cups)
    return cups

#Ask player to guess where is the ball
def player_guess():
    guess = input("Pick a cup: 1, 2 or 3: ")
    
    while guess not in ["1","2","3"]:
        guess = input("Please only 1, 2 or 3: ")
    
    return guess

#Check if player's guess is correct
def check_guess(guess,shuffled_cups):
    
    if shuffled_cups.index("O") == int(guess)-1:
        print("Correct!")
        print(shuffled_cups)
    else:
        print("Wrong")
        print(shuffled_cups)
        
#Ask if player wants to play again
def replay():
    replay = input("Want to play again? Y or N: ")
    
    while replay.lower() not in ("y", "n"):
        replay = input("Please only Y or N: ")
    
    return replay
    


#GAME SCRIPT


print("Welcome to the Cups Game!")

while True:
    ready_ans = ready()
    if ready_ans.lower() == "y":
        print("Let's go!")
        game_on = True
    elif ready_ans.lower() == "n":
        print("Come back soon!")
        break

    while game_on:

        cups = ["O"," "," "]
        shuffled_cups = shuffle_cups(cups)

        guess = player_guess()
        check_guess(guess,shuffled_cups)
        break

    lets_replay = replay()
    if lets_replay.lower() == "y":
        print("Let's go!")
        
    elif lets_replay.lower() == "n":
        print("Thanks for playing!")
        break
        
