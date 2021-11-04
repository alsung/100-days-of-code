# Day 18 Turtle Exercise

from turtle import Turtle, Screen, shape
import random

tommy = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "thistle"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tommy.forward(100)
        tommy.right(angle)



for shape_side_n in range(3, 11):
    tommy.color(random.choice(colors))
    draw_shape(shape_side_n)




























screen = Screen()
screen.exitonclick()