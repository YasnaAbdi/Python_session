from turtle import Turtle, Screen
import random

timmy_turtle = Turtle()

#timmy_turtle.forward(100)
#timmy_turtle.right(90)
#timmy_turtle.forward(100)
#timmy_turtle.right(90)
#timmy_turtle.forward(100)
#timmy_turtle.right(90)
#timmy_turtle.forward(100)

#round = 3
#for _ in range(10):
#    round += 1
#    for _ in range(round):
#        timmy_turtle.forward(100)
#        rotate = 360/round
#        timmy_turtle.right(rotate)
#colors = ["red", "orange", "pink", "green", "purple", "orange", "blue"]
#turn = [90, 180, 270, 360]


#timmy_turtle.shape("circle")
#timmy_turtle.pensize(5)
#timmy_turtle.speed(10)
#while True:
#    pick_color = random.choice(colors)
#    random_turn = random.choice(turn)
#    timmy_turtle.color(pick_color)
#    timmy_turtle.forward(30)
#    timmy_turtle.right(random_turn)

for i in range(100):
 timmy_turtle.circle(i)





screen = Screen()
screen.exitonclick()


