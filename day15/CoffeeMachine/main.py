MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_money = 0

# TODO: Prompt user asking "What would you like? (espresso/latte/cappucino): "
    # Check user's input
    # Prompt should show every time action has completed, e.g. once drink is 
        # dispensed. Show again to serve next customer. 

selection = input("What would you like? (espresso/latte/cappuccino): ")


# TODO 2: Turn off machine by entering "off" to prompt
    # Code should end execution 

if selection == "off":
    print("Goodbye!")
    quit()

# TODO 3: Print report
    # When user enters 'report' to prompt, report should show current resource
        # levels. 
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5

elif selection == "report":
    for res in resources:
        print(f"{res.title()}: {resources[res]}")
    print(f"Money: ${machine_money}")

# TODO 4: Check resources sufficient?
    # When user chooses drink, check if enough resources to make drink
    # if Latte requires 200ml water but only 100ml left in machine, print 
        # “​Sorry there is not enough water.​"
    # Same should happen if another resource is depleted

# TODO 5: Process coins
    # If resources are sufficient to make drink, prompt user to insert coins
    # Quarters = $0.25, Dimes = $0.10, Nickels = $0.05, Pennies = $0.01
    # Calculate monetary value of coins inserted. E.g. 1 quarter, 2 dimes, 
        # 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO 6: Check transation successful
    # Check user has inserted enough money to purchase selected drink
    # e.g. Latte cost $2.50, but only inserted $0.52 then after counting 
        # the coins, print "Sorry that's not enough money. Money refunded."
    # If user has inserted enough money, then the cost of drink gets added to
        # machine as profit and will be reflected next time report is triggered.
        # e.g.: 
            # Water: 100ml
            # Milk: 50ml
            # Coffee: 76g
            # Money: $2.5
    # If user inserted too much money, machine should offer change
        # e.g. "Here is $2.45 dollars in change". Change rounded to 2 decimals

# TODO 7: Make coffee
    # If transaction successful and enough resources to make drink, then 
        # ingredients to make drink should be deducted from resources

        # e.g. report before purchasing latte:
        # Water: 300ml
        # Milk: 200ml
        # Coffee: 100g
        # Money: $0

        # report after purchasing:
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5

    # Once resources deducted, tell user "Here is your latte. Enjoy!"