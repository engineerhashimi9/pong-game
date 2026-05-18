from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.teleport(pos[0], pos[1])
        self.setheading(90)

    def move_upp(self):
        self.forward(30)

    def move_down(self):
        self.backward(30)
