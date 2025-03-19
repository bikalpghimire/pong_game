import random
from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        start_heading = [randint(135,225), randint(-45, 45)]
        self.setheading(random.choice(start_heading))
        self.move_speed = 0.1
    def move(self):
        self.forward(10)

    def bounce_wall(self):
        self.setheading(self.heading() * -1)

    def bounce_paddle(self):
        self.setheading(180 - self.heading())
        self.move_speed *= 0.5
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        if -90 < self.heading() < 90:
            self.setheading(randint(135, 225))
        else:
            self.setheading(randint(-45, 45))