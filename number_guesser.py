import random

print("Welcome to Number Guesser!")

while True:
    top_of_range = input("Type your preferred range of numbers to guess from: ")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("Please type a number greater than 0: ")
            continue 
    else:
        print("Please numbers only: ")
        continue
    break

random_number = random.randint(1,top_of_range)

guesses = 0
while True:
    
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number: ")
        continue

    if user_guess == random_number:
        guesses += 1
        print("You Win!")
        print(f"You guessed {guesses} times")
        print("Thanks for playing")
        break
    elif user_guess > random_number:
        guesses += 1
        print("You are above the number. Try again.")
        print(f"Guess Counter: {guesses}")
        continue
    else:
        guesses += 1
        print("You are below the number. Try again.")
        print(f"Guess Counter: {guesses}")
        continue