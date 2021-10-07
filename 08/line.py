import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    a = (y2 - y1) / (x2 - x1)
    b = y1 - x1 * a
    for x in range(x1, x2 + 1, 10):
        y = a * x + b
        draw_point((x, y))

    draw_point(p2)  # 최종적인 점을 찍어준다.
    pass


def sub_draw_line(p1, p2, right):
    curvature = 2  # 곡률

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2,

    if right:
        x3, y3 = mid_x - (mid_y - y1) * curvature, mid_y + (mid_x - x1) * curvature
    else:
        x3, y3 = mid_x + (mid_y - y1) * curvature, mid_y - (mid_x - x1) * curvature

    for i in range(0, 50 + 1, 2):
        t = i / 50
        sub_x1, sub_y1 = (1 - t) * x1 + t * x3, (1 - t) * y1 + t * y3
        sub_x2, sub_y2 = (1 - t) * x3 + t * x2, (1 - t) * y3 + t * y2
        x, y = (1 - t) * sub_x1 + t * sub_x2, (1 - t) * sub_y1 + t * sub_y2
        draw_point((x, y))

    draw_point(p2)


def draw_line(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    mid_x, mid_y = (x1 + x2)/2, (y1 + y2)/2,

    sub_draw_line((x1, y1), (mid_x, mid_y), True)
    sub_draw_line((mid_x, mid_y), (x2, y2), False)

    # x3, y3 = mid_x - (mid_y - y1), mid_y + (mid_x - x1)
    #
    # for i in range(0, 100 + 1, 2):
    #     t = i / 100
    #     sub_x1, sub_y1 = (1 - t) * x1 + t * x3, (1 - t) * y1 + t * y3
    #     sub_x2, sub_y2 = (1 - t) * x3 + t * x2, (1 - t) * y3 + t * y2
    #     x, y = (1 - t) * sub_x1 + t * sub_x2, (1 - t) * sub_y1 + t * sub_y2
    #     draw_point((x, y))
    pass


prepare_turtle_canvas()

draw_line((-200, -150), (200, 200))

turtle.done()