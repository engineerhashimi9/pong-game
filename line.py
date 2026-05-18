from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pensize(3)
        self.speed("fastest")
        self.run()

    def run(self):
        self.teleport(0, -290)
        self.setheading(90)
        for i in range(30):
            self.penup()
            self.forward(10)
            self.pendown()
            self.forward(10)
