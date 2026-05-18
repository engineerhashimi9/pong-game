from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left = 0
        self.right = 0
        self.goto(-100, 190)
        self.write(self.left, False, "center", ("courier", 80, "normal"))
        self.goto(100, 190)
        self.write(self.right, False, "center", ("courier", 80, "normal"))

    def draw(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.left, False, "center", ("courier", 80, "normal"))
        self.goto(100, 190)
        self.write(self.right, False, "center", ("courier", 80, "normal"))

    def incress(self, p):
        if p == 1:
            self.left += 1
        elif p == 2:
            self.right += 1
        self.draw()
