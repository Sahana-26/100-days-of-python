from turtle import *
from Snake_game import Snake
import time
s= Screen()

s.setup(width=500,height=400)
s.bgcolor("black")
s.title("Snake game")
s.tracer(0)

snake = Snake()
    
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

s.exitonclick()