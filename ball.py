from turtle import Turtle
from random import randint as rnd


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(1)
        self.penup()
        self.y = 10
        self.x = 10

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)
        if abs(self.ycor()) > 280:
            self.y *= -1

    def detect(self):
        self.x *= -1
