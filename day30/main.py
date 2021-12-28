"""
Try Except Else Finally pattern

try: something that might cause an exception
except: do this if there WAS an exception
else: do this if there were NO exceptions
finally: do this no matter what happens
"""

# #FileNotFound
try: 
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else: # if no exceptions are caught
    content = file.read()
    print(content)
finally: # runs no matter what
    raise TypeError("This is an error i made up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

