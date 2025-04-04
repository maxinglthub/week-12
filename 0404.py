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

x_list = [1, 3, 4, 5]
y_list = [2, 4, 6, 8]

print(x_list, y_list)

i = 0
factor = 20

while i < len(x_list):
    pen.goto(factor * x_list[i], factor * y_list[i])
    pen.stamp()
    i = i + 1

sigma_x = 0
i = 0

while i < len(x_list):
    sigma_x = sigma_x + x_list[i]
    i = i + 1
print(sigma_x)