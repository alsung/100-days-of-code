# Treasure Island Project Day 3.6
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''') # to print multiple lines, use ''' '''
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
if choice1.lower() == "left":
    choice2 = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if choice2.lower() == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n")
        if choice3.lower() == "blue":
            print("You enter a room of beasts. Game Over.")
        elif choice3.lower() == "red": 
            print("You enter a room of fire and get burned by fire. Game Over.")
        elif choice3.lower() == "yellow":
            print("Congratulations! You found the treasure! You Win!")
        else: 
            print("You fall into a booby trap. Game Over.")
    else:
        print("You got eaten by sharks. Game Over.")
else:
    print("You fell into a hole. Game Over.")