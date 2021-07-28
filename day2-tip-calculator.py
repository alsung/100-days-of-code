# Day 2 of 100 Days of Code - Python Bootcamp 2021 - Dr. Angela Yu

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places. 

print("Welcome to the tip calculator.")
bill_total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

tip_value = float(f"1.{tip}")
total_with_tip = bill_total * tip_value
total_per_person = round(total_with_tip / num_people, 2)
final_amount = "{:.2f}".format(total_per_person)
print(f"Each person should pay: ${final_amount}")
