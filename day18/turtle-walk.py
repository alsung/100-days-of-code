# Day 18 Turtle Exercise

from turtle import Turtle, Screen, colormode, shape
import random

tommy = Turtle()
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "thistle"]
directions = [0, 90, 180, 270]
tommy.pensize(10)
tommy.speed("fastest")

for _ in range(200):
    tommy.color(random_color())
    tommy.forward(30)
    tommy.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()