# Lab6B.py
# A simple guessing game where the user guesses a random number

import random
secret = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! The number was", secret)
        break
