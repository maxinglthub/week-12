import turtle
import random

wn = turtle.Screen()
wn.setup(width=600, height=600)

pen = turtle.Turtle()
pen.speed(0)

pen.backward(300)
pen.forward(600)
pen.penup()
pen.goto(0, 300)
pen.pendown()
pen.goto(0, -300)
pen.penup()

x_list = []
y_list = []

while len(x_list) < 10:
    x_list.append(random.randint(-5, 5))
    y_list.append(random.randint(-5, 5))

print(x_list, y_list)

i = 0
factor = 20

while i < len(x_list):
    pen.goto(factor * x_list[i], factor * y_list[i])
    pen.stamp()
    i = i + 1

#test