from turtle import *
from Snake_game import Snake
from food import Food
from score_board import Scoreboard
import time
s= Screen()

s.setup(width=600,height=600)
s.bgcolor("black")
s.title("Snake game")
s.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
s.onkey(snake.down, "Down")

game_on = True
while game_on:
    s.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()  

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

s.exitonclick()