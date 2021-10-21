# Day 12.1 Guess the Number Game

# Print Prompts
# Choose a random number between 1 and 100
# Make a function to set difficulty
# Let the user guess a number
# Function to check user's guess against actual answer.
# Track the number of turns and reduce by 1 if they get it wrong.
# Repeat the guessing functionality if they got it wrong. 

import art
import random

# print logo and prompt user
print(art.logo)

def check_answer(guess, answer):
    if guess > answer: 
        print("Too high.")
    elif guess < answer:
        print

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    num_attempts = 0

    # computer chooses a number between 1 and 100
    computer_number = random.randint(1, 100)
    print(computer_number)

    if difficulty == 'easy':
        num_attempts = 10
    else:
        num_attempts = 5

    guess_correctly = False

    while num_attempts > 0:
        print(f"You have {num_attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > computer_number:
            print("Too high.")
        elif guess < computer_number:
            print("Too low.")
        else: 
            guess_correctly = True
            print(f"You got it! The answer was {computer_number}.")
            return

        if num_attempts > 1:
            print("Guess again.")
        num_attempts -= 1

    if num_attempts == 0 and guess_correctly == False:
        print("You've run out of guesses, you lose.")

play_game()

