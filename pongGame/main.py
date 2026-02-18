from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Kos Nanat")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(x=350, y=0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


paddle.listen()
paddle.onkey(go_up(), "Up")
paddle.onkey(go_down(), "Down")


screen.exitonclick()
