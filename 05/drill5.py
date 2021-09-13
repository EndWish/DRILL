import turtle

def go():
    turtle.stamp()
    turtle.forward(50)

def move_up():
    turtle.setheading(90)
    go()

def move_down():
    turtle.setheading(270)
    go()

def move_right():
    turtle.setheading(0)
    go()

def move_left():
    turtle.setheading(180)
    go()

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(move_up, 'W')
turtle.onkey(move_up, 'w')
turtle.onkey(move_down, 'S')
turtle.onkey(move_down, 's')
turtle.onkey(move_left, 'A')
turtle.onkey(move_left, 'a')
turtle.onkey(move_right, 'D')
turtle.onkey(move_right, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()

turtle.exitonclick()
