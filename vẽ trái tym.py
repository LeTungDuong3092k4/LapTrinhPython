import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)
t.color("red")

t.begin_fill()
t.left(140)
t.forward(200)
t.circle(-100, 200)
t.left(120)
t.circle(-100, 200)
t.forward(200)
t.end_fill()


t.hideturtle()


screen.exitonclick()