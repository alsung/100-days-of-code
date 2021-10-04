# Randomization Exercise Day 4.1

# Heads or Tails

"""
Instructions:
Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 
Important, the first letter should be capitalized. 
There are many ways of doing this. But to practice, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails. 
"""

# 1 means Heads and 0 means Tails

import random

flip = random.randint(0, 1)
if flip == 0:
    print("Tails")
else: 
    print("Heads")