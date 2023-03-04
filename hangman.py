import random

print("\n")
print("Welcome to Hangman!")
word_bank = ["kangaroo", "apple", "padel", "sports", "music", "spiderman", 
             "macintosh", "programming", "apex", "playstation", "engineer", 
             "software", "iphone", "ironman", "vancouver", "canada", "developer", 
             "code", "velociraptor", "phoenix", "crown", "sierra", "laboratory", 
             "data", "password", "encyclopedia", "jupyter", "saturn", "universe", 
             "black", "polygon", "education", "travel", "gaming", "planet", "hamburger", 
             "pizza", "mexico", "italy", "brazil", "football", "golf", "tennis", 
             "success", "alternator", "devotion", "peacekeeper", "nemesis", "octane", 
             "pathfinder", "water", "orange", "banana", "sunglasses", "backpack", 
             "tournament", "ball", "schwarzenegger", "thermodynamics", "science", 
             "numbers", "javascript", "python", "framework", "world", "xylophone", 
             "guitar", "piano", "crocodile", "cellular", "makeup", "dance", "microphone",
             "drums", "bass", "fishing", "book", "magic", "space", "city", "rock",
             "instrument", "triangle", "jungle", "animal", "restaurant", "food", "drink",
             "alcohol", "chocolate", "energy", "apartment", "keyboard", "computer",
             "wonder", "movies", "whiplash", "internet", "stellar", "light", "proton",
             "neutron", "boy", "gianluca", "cynthia", "beach", "vacations", "pool",
             "summer", "winter", "autumn", "spring", "plants", "palm", "racket",
             "court", "artist", "emotion", "mind", "conciousness", "life", "death",
             "phylosohpy", "headphones", "airplane", "rocket", "mountain", "hiking",
             "king", "queen", "cards", "dogs", "cats", "rocky", "bowie", "element",
             "physics", "chemistry", "technology", "ecosystem", "habitat", "forest",
             "desert", "midnight", "moon", "laser", "superhero", "chicken", "circle",
             "sphere", "flowers", "dinosaur", "ghost", "phantom", "skateboard",
             "touchscreen", "television", "radio", "friday", "jarvis", "xbox", "time",
             "minutes", "love", "obsession", "mississippi", "pickle", "zebra",
             "walrus", "question", "igloo", "quantum", "axe", "taxi", "vanguard",
             "vicious", "vertebrae", "spine", "skeleton", "muscles", "sight",
             "landscape", "sunset", "sunrise", "dark", "vacuum", "joystick", "cold",
             "plastic", "metal", "basketball", "swimming", "olympics", "dwarf",
             "elves", "rings", "wizard", "gryffin", "giant", "bycicle", "scooter",
             "friends", "independent", "sexual", "hope", "skill", "awesome", "coffee",
             "note", "notebook", "kitchen", "war", "clouds", "connection", "pyramid",
             "tesseract", "infinity", "robotics", "intellience", "artificial", "bugs",
             "cartoon", "network", "knight", "tuxedo", "sword", "spell"]

playing = True

while True:
    ready = input("Are you ready to play?: ").lower()
    if ready == "yes":
        print("Let's go!", "\n")
        playing = True
        break
    elif ready == "no":
        print("Come back soon!")
        playing = False
        break
    else:
        print("Please write Yes or No")
        continue

while playing:
    word_choice = random.choice(word_bank).upper()
    word_letters = set(word_choice)
    guessed_letters = set()
    counter = 0
    lives = 5
    print(f"Starting lives: {lives}")

    while len(word_letters) > 0:

        print("Used letters: ", " ".join(guessed_letters))

        word_list = [letter if letter in guessed_letters else "-" for letter in word_choice]
        print("The word is: ", " ".join(word_list))

        user_choice = input("Guess a letter: ").upper()

        if user_choice.isalpha():
            print("\n")
            if user_choice == word_choice:
                counter += 1
                break
            elif len(user_choice) > 1:
                print("Please only choose 1 letter.")
            else:
                if user_choice in guessed_letters:
                    print("You already tried that letter. Choose another.")
                else:
                    if user_choice in word_letters:
                        counter += 1
                        lives += 1
                        guessed_letters.add(user_choice)
                        word_letters.remove(user_choice)
                        if len(word_letters) > 0:
                            print("Nice!")
                            print(f"Lives left: {lives}")
                    elif user_choice not in word_letters:
                        if lives > 0:
                            counter += 1
                            lives -= 1
                            guessed_letters.add(user_choice)
                            if lives == 0:
                                print("Out of lives! The man has been hanged XP")
                                print(f"The word was: {word_choice}")
                                break
                            else:
                                print("Try again!")
                                print(f"Lives left: {lives}")
        else:
            print("Letters only.")
            
    if lives >= 1:
        print("\n")
        print(f"Well done! You made {counter} guesses")
        print(f"The word was: {word_choice}")

    while True:
        play_again = input("Do you want to play again? ").lower()

        if play_again == "no":
            print("Thanks for playing!", "\n")
            playing = False
            break
        elif play_again == "yes":
            print("Let's go!", "\n")
            playing = True
            break
        else:
            print("Please only Yes or No")
            continue
    








