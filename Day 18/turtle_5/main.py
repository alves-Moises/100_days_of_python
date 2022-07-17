from pickletools import float8
from turtle import Turtle, Screen
from random import choice

turt = Turtle()

def rand_color():
    return  choice(["blue", "pink", "black"])

for i in range(3, 10):
    turt.color(rand_color(), rand_color())
    for j in range(i):
        turt.forward(100)
        turt.right(360 / i)


screen = Screen()
screen.exitonclick()