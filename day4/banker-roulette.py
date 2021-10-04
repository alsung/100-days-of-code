# Banker Roulette - Who will pay the bill? Exercise Day 4.2
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

names_len = len(names)
# rand_idx = random.randint(0, names_len - 1)
# bill_payer = names[rand_idx]

bill_payer = random.choice(names)

print(f"{bill_payer} is going to buy the meal today!")