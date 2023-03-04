print("Welcome to my Python Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("See you soon!")
    quit()

print("Okay, let's play!")

points = 0

answer = input("What does CPU stand for? ")

if answer == "central processing unit":
    print("Correct!")
    points += 1
else:
    print("Incorrect")

print(f"Your total score is: {points}")

answer = input("What color is the sky? ")

if answer == "blue":
    print("Correct!")
    points += 1
else:
    print("Incorrect")

print(f"Your total score is: {points}")

answer = input("What is the shape of a ball? ")

if answer == "sphere":
    print("Correct!")
    points += 1
else:
    print("Incorrect")

print(f"Your total score is: {points}")
print(f"You got {int((points/3)*100)}%")