score = 0
print("Welcome to the Valorant Quiz Game!") # Welcome message

playing = input("Would you like to play? '(Y/N)'") # Option to play or not
if playing == "y":
    name = input("Before we begin, what is your name? ") # Player enters their name
    print("Hello ",name)

    answer = input("Is Jett a duelist? ") # First question
    if answer == "yes":
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    print("Next question!")

    answer = input("Is Brimstone a controller? ") # Second question
    if answer == "yes":
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    print("Next question!")

    answer = input("Is Reyna a duelist? ") # Third question
    if answer == "yes":
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    print("Next question!")

    answer = input("Is Viper a duelist? ") # Fourth question
    if answer == "no":
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    print("Next question!")

    answer = input("Is Chamber a sentinel? ") # Fifth question
    if answer == "yes":
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    print("Congratulations " + str(name) + " you have completed the quiz!\nYou got " + str(score) + " out of 5 questions correct!") # End and results of the quiz

elif playing == "n":
    print("Goodbye!")
    quit()
else: print("Invalid selection try again")