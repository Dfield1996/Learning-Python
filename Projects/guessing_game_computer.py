import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number which is between 1 and {x}: '))
        if guess < random_number:
            print("Incorrect, try guessing higher.")
        elif guess > random_number:
            print("Incorrect, try guessing lower.")

    print(f'Correct!, you guessed the number {random_number}!')


guess(10)