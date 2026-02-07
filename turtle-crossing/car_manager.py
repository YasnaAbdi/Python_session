import random
from turtle import Turtle
import random
 
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(20, 40)
        self.color(random.choice[COLORS])

