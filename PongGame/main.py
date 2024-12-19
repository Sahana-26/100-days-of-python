from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

s = Screen()
s.listen()

s.tracer(0)
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball((0,0))
score = ScoreBoard()

s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")

s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    print(ball.move_speed)
    s.update()
    ball.move()

    # Detection of collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detection of collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Reset the ball position
    if ball.xcor() > 400:
        ball.reset()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()


s.exitonclick()