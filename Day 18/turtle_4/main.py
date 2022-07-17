from turtle import Screen, Turtle

turtle = Turtle()
turtle.shape("turtle")

for i in range(1000):
    turtle.pendown()
    turtle.forward(10)
    # turtle.dot(5)

    turtle.penup()
    turtle.forward(10)


screen = Screen()
screen.exitonclick()
