###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram, random
from turtle import Turtle, Screen, position
import turtle as t

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

color_list = rgb_colors

print(color_list)
def random_color(colors):
    color = random.choice(colors)
    r = color[0]
    g = color[1]
    b = color[2]
    return ((r, g, b))


tort = Turtle()

tort.speed('fastest')

tort.pensize(30)
t.colormode(255)
tort.penup()
tort.dot(20, random_color(color_list))
i = 0

while i < 1000:
    tort.setpos(x=0, y=i)
    for j in range(10):
        tort.pendown()
        tort.color(random_color(color_list))
        tort.forward(0)

        tort.penup()
        tort.forward(30)
    i += 30


screen = Screen()
screen.exitonclick()

