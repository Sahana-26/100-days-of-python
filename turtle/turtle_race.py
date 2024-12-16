from turtle import Turtle,Screen
import random

s= Screen()
s.setup(width=500,height=400)

is_race_on = False

colors = ["red","yellow","green","blue","brown"]

color = s.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color \n")

if color in colors:
    is_race_on= True

all_turtles = []

for i in range(5):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(x=-240, y=-100+(i*50))
    all_turtles.append(t)

while is_race_on:
    for i in all_turtles:
        if i.xcor() >230:
            is_race_on=False
            if color == i.pencolor():
                print(f"you won, {color} won the game!!")
            else:
                print(f'you lost, {i.pencolor()} won the game!!')
            
        i.forward(random.randint(0,10))

s.exitonclick()
