# Day 4.4 Rock Paper Scissors Project 

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice >= 3 or player_choice < 0:
    print("Invalid number.")
else:
    print(game_images[player_choice])

    comp_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[comp_choice])

    if player_choice == 0 and comp_choice == 2:
        print("You win!")
    elif comp_choice == 2 and player_choice == 0:
        print("You lose!")
    elif comp_choice > player_choice:
        print("You lose!")
    elif player_choice > comp_choice:
        print("You win!")
    elif comp_choice == player_choice:
        print("It's a draw")

