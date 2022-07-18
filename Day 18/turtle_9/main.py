import turtle as t
import random
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

# tim.pensize(30)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return ((r, g, b))


for i in range(360):
    tim.color(random_color())
    tim.right(10)

    for j in range(360):
        tim.circle(50)

        tim.forward(1)
        tim.right(1)

