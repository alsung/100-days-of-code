# Day 18 Turtle Exercise 
# Spirograph

from turtle import Turtle, Screen, colormode, shape
import random

tommy = Turtle()
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tommy.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tommy.color(random_color())
        tommy.setheading(tommy.heading() + 10)
        tommy.circle(100)



draw_spirograph(5)


screen = Screen()
screen.exitonclick()