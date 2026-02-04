from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()

    def writScore(self):
        new_score = 0
        score = Score()
        score.color("white")
        score.penup()
        score.hideturtle()
        score.goto(0, 260)
        score.write(arg=f"score: {new_score}", align="center", font=("Ariel", 20, "normal"))

    def updateScore(self):
        if
