import art
import game_data
import random
import os

# Generate random account from game data. 
# Format account data into printable format
# Ask user for a guess.
# Check if user is correct
## Get follower count of each account
## If statement to check if user is correct
# Give user feedback on their guess.
# Score keeping
# Make game repeatable
# Make B become the next A
# Add art
# clear screen between rounds

def clear():
    """Clears the console."""
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def get_random_account():
    """Get data from a random account in game_data.data."""
    return random.choice(game_data.data)

def format_data(account):
    """Format account into printable format: name, description, and country."""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}."

def check_guess(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it 
    right. Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def game():
    # print logo
    print(art.logo)
    score = 0
    game_should_continue = True

    # retrieve first entry from game_data.data
    a_account = get_random_account()
    b_account = get_random_account()

    while game_should_continue:
        a_account = b_account
        b_account = get_random_account()

        while a_account == b_account:
            b_account = get_random_account()
    
        # print "Compare A: " + name, description, and country
        print(f"Compare A: {format_data(a_account)}")

        # print vs logo
        print(art.vs)

        # print "Against B: " + name, description, and country
        print(f"Against B: {format_data(b_account)}")

        # ask who has more followers: A or B
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = a_account['follower_count']
        b_follower_count = b_account['follower_count']
        is_correct = check_guess(guess, a_follower_count, b_follower_count)
        # print(f"a_follower_count = {a_follower_count}")
        # print(f"b_follower_count = {b_follower_count}")
        # print(is_correct)

        clear()
        print(art.logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()