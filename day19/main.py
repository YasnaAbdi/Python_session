from turtle import Turtle, Screen

point = Turtle()
screen = Screen()

def go_forward():
    point.forward(40)

def go_backward():
    point.backward(40)

def counter_clock_wise():
    point.left(10)


def clock_wise():
    point.right(10)


def clear():
    point.clear()
    

screen.listen()
screen.onkey(fun=go_forward, key="w")
screen.onkey(fun=go_backward, key="s")
screen.onkey(fun=counter_clock_wise, key="a")
screen.onkey(fun=clock_wise, key="d")
screen.onkey(fun=clear, key="c")
screen.exitonclick()