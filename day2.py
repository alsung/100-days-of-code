# Day 2 of 100 Days of Code - Python Bootcamp 2021 - Dr. Angela Yu

# Number Manipulation
divide = 8 / 3
floor_divide = 8 // 3 # returns the floor integer of the evaluation

print(divide)
print(floor_divide)

print(round(8 / 3, 3)) # returns rounded int value if decimal places not specified

# F-strings
# allows users to print non-string values without casting to string
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# Exercise
# simple command-line program calculates how many days, months, and weeks you have left
# if user were to live to age 90. 
age = input("What is your current age? ")

age_as_int = int(age)
years_remaining = 90 - age_as_int
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365 

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

