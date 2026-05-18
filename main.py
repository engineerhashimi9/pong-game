from turtle import Turtle, Screen
from line import Line
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

## seting the screen
sc = Screen()
sc.setup(800, 600)
sc.bgcolor("black")
sc.tracer(0)
# making ojects
line = Line()
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
score = ScoreBoard()
# events
sc.listen()
sc.onkeypress(left_paddle.move_upp, "w")
sc.onkeypress(left_paddle.move_down, "s")
sc.onkeypress(right_paddle.move_upp, "Up")
sc.onkeypress(right_paddle.move_down, "Down")

player = 1
while True:
    sc.update()
    time.sleep(0.05)
    if abs(ball.xcor()) > 320 and (
        ball.distance(left_paddle) < 50 or ball.distance(right_paddle) < 50
    ):
        ball.detect()
        ball.x += 5
        ball.y += 5
        player = 1 if player == 2 else 2
    if abs(ball.xcor()) > 380:
        ball.teleport(0, 0)
        sc.update()
        ball.detect()
        ball.y, ball.x = (10, 10)
        score.incress(player)
        time.sleep(2)
        player = 1 if player == 2 else 2

    ball.move()


###
sc.mainloop()
