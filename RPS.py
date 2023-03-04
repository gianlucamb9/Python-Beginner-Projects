import random

print("Welcome to Rock, Paper Scissors!")
player_score = 0
computer_score = 0

while True:
    player_choice = input("Choose Rock, Paper or Scissors: ")
    choice_list = ["rock", "paper", "scissors"]

    if player_choice.lower() not in choice_list:
        print("Please chose Rock, Paper or Scissors")
        continue
    else:
        print(f"You have chosen {player_choice}.")

    computer_choice = random.choice(choice_list)
    print(f"Computer choses: {computer_choice}")

    if player_choice == computer_choice:
        print("Tie round!")
        print(f"Score is: Player {player_score} - Computer {computer_score}")
    elif player_choice == "rock" and computer_choice == "paper":
        print("Computer wins the round")
        computer_score += 1
        print(f"Score is: Player {player_score} - Computer {computer_score}")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win the round")
        player_score += 1
        print(f"Score is: Player {player_score} - Computer {computer_score}")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win the round")
        player_score += 1
        print(f"Score is: Player {player_score} - Computer {computer_score}")
    elif player_choice == "paper" and computer_choice == "scissors":
        print("Computer wins the round")
        computer_score += 1
        print(f"Score is: Player {player_score} - Computer {computer_score}")
    elif player_choice == "scissors" and computer_choice == "rock":
        print("Computer wins the round")
        computer_score += 1
        print(f"Score is: Player {player_score} - Computer {computer_score}")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win the round")
        player_score += 1
        print(f"Score is: Player {player_score} - Computer {computer_score}")

    while True:
        play_again = input("Do you want to play again? Y or N: ")

        if play_again.lower() == "y":
            print("Let's go!")
            break
        elif play_again.lower() == "n":

            if player_score == computer_score:
                print(f"Final score: Player {player_score} - Computer {computer_score}")
                print("Tie game!")
            elif player_score > computer_score:
                print(f"Final score: Player {player_score} - Computer {computer_score}")
                print("You win the game!")
            else:
                print(f"Final score: Player {player_score} - Computer {computer_score}")
                print("Computer wins the game")

            print("Come back soon!")
            player_score = 0
            computer_score = 0
            break
        else:
            print("Please only Y or N")
            continue

    if play_again != "y":
        break
    else:
        continue