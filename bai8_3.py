import turtle
import random

colors = ["red", "green", "blue"]

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

for i in range(12):
    pen.pencolor(colors[i % 3])
    pen.circle(100)
    pen.left(30)
    pen.setposition(0, 0)

turtle.done()
