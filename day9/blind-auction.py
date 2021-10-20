# Day 9.3 Blind Auction

import os

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# print logo
import art
print(art.logo)

bid_dict = {}
other_bids = "yes"

while other_bids == "yes":
    # ask for Name input
    name = input("What is your name?\n")

    # ask for bid price
    bid_price = int(input("What is your bid price? $"))

    # add name and bid price to dictionary
    bid_dict[name] = bid_price

    # ask if there are other uses who want to bid
    other_bids = input("Are there other bidders? Type 'yes' or 'no'.\n")

    
    
    clear()
    
if other_bids == "no":
    highest_bid = 0
    highest_bidder = ""
    for name in bid_dict:
        if bid_dict[name] > highest_bid:
            highest_bid = bid_dict[name]
            highest_bidder = name
    
    print(f"The winner is {highest_bidder} with ${highest_bid}.")