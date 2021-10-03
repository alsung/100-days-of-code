# Love Calculator Challenge Day 3.5

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
combined_lower = combined_string.lower()

t = combined_lower.count("t")
r = combined_lower.count("r")
u = combined_lower.count("u")
e = combined_lower.count("e")

true = t + r + u + e

l = combined_lower.count("l")
o = combined_lower.count("o")
v = combined_lower.count("v")
e = combined_lower.count("e")

love = l + o + v + e

love_score = true * 10 + love

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like code and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")