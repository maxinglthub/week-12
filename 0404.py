import turtle

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
sigma_y = 0
sigma_xx = 0
sigma_xy = 0
i = 0

while i < len(x_list):
    sigma_x = sigma_x + x_list[i] #x加總
    sigma_y = sigma_y + y_list[i] #y加總
    sigma_xx = sigma_xx + x_list[i] * x_list[i] #x加總的平方
    sigmna_xy = sigma_xy + y_list[i] * y_list[i]
    i = i + 1

print(sigma_x, sigma_y, sigma_xx)


#-------

n = len(x_list)

xbar = sigma_x / n
ybar = sigma_y / n

upfloor = (sigma_xy) - (n * xbar * ybar)
dowfloor = (sigma_xx) - n * (xbar * xbar)

answer_a = upfloor / dowfloor
answer_b = ybar - (answer_a * xbar)
print(answer_a, answer_b)

pen.goto(min(x_list) * factor, (answer_a * min(x_list) + answer_b) * factor)
pen.pendown()
pen.goto(max(x_list) * factor, (answer_a * max(x_list) + answer_b) * factor)

wn.exitonclick()
