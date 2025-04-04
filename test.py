import turtle
import random


wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.setworldcoordinates(-10, -10, 110, 110)  
wn.title("Linear Regression Visualization")


factor = 100 / 5  


axis = turtle.Turtle()
axis.hideturtle()
axis.speed(0)
axis.penup()
axis.goto(0, 50)
axis.pendown()
axis.goto(100, 50)  
axis.penup()
axis.goto(50, 0)
axis.pendown()
axis.goto(50, 100)  

pen = turtle.Turtle()
pen.shape("circle")
pen.color("red")
pen.penup()
pen.speed(0)

x_list = []
y_list = []

while len(x_list) < 4:
    x = random.randint(0, 5)
    y = random.randint(0, 5)
    x_list.append(x)
    y_list.append(y)

n = len(x_list)
x_mean = sum(x_list) / n
y_mean = sum(y_list) / n

sum_xy = sum([x_list[i] * y_list[i] for i in range(n)])
sum_x2 = sum([x_list[i] ** 2 for i in range(n)])
a = (sum_xy - n * x_mean * y_mean) / (sum_x2 - n * x_mean ** 2)


b = y_mean - a * x_mean

print("x_list =", x_list)
print("y_list =", y_list)
print(f"回歸直線: y = {a:.2f}x + {b:.2f}")

for i in range(n):
    x_screen = x_list[i] * factor
    y_screen = y_list[i] * factor
    pen.goto(x_screen, y_screen)
    pen.stamp()

line = turtle.Turtle()
line.color("blue")
line.penup()
x_start = 0
x_end = 5
y_start = a * x_start + b
y_end = a * x_end + b
line.goto(x_start * factor, y_start * factor)
line.pendown()
line.goto(x_end * factor, y_end * factor)

turtle.done()