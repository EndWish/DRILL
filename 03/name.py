import turtle

#김
turtle.forward(50)
turtle.goto(0,-100)

turtle.penup()
turtle.goto(80, 0)
turtle.pendown()

turtle.right(90)
turtle.forward(100)

turtle.penup()
turtle.goto(0,-120)
turtle.pendown()

turtle.forward(40)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(80)

#시
turtle.penup()
t1 = (170,0)    #그리도 한번 튜플 이용해 봤습니다.
turtle.goto(t1) 
turtle.pendown()

turtle.goto(100,-100)
turtle.goto(135,-50)
turtle.goto(170,-100)

turtle.penup()
t2 = (190,0)
turtle.goto(t2) 
turtle.pendown()


turtle.left(90)
turtle.forward(100)

#인
turtle.penup()
t3 = (200,-50)
turtle.goto(t3) 
turtle.pendown()

turtle.circle(30)

turtle.penup()
t4 = (280,0)
turtle.goto(t4) 
turtle.pendown()

turtle.forward(100)

turtle.penup()
t5 = (230,-120)
turtle.goto(t5) 
turtle.pendown()

turtle.forward(40)
turtle.left(90)
turtle.forward(70)

turtle.exitonclick()








