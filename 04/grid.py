import turtle

p1 = [-250,-350]
p2 = [-350,-250]

count = 6
while (count > 0):
    turtle.penup()
    p1[1] += 100
    turtle.goto(p1)
    turtle.pendown()
    turtle.forward(500)
    count -= 1

turtle.left(90)

count = 6
while (count > 0):
    turtle.penup()
    p2[0] += 100
    turtle.goto(p2)
    turtle.pendown()
    turtle.forward(500)
    count -= 1

turtle.exitonclick()
