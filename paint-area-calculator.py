# Day 8.1 Paint Area Calculator

"""
You are painting a wall. the instructions on the paint can says that 1 can of 
paint can cover 5 square meters of wall. Given a random height and width of 
wall, calculate how many cans of paint you'll need to buy. 

number of cans = (wall height * wall width) / coverage per can
"""
import math

def paint_calc(height, width, cover):
    total_area = height * width
    num_cans = total_area / cover
    num_cans = int(math.ceil(num_cans))
    print(f"You'll need {num_cans} cans of paint.") 

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)