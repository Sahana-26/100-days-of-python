from turtle import Turtle,Screen
import random

t = Turtle()

# draw a square using turtle module

for _ in range(4):
    t.width(5)
    t.forward(100)
    t.left(90)

# dashed line

length = 200
while(length):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)
    length-=20


# triangle,square,pentagon,hexagon,heptagon,octagon,nanogon

colors = [
    "#000080",  # navy
    "#FFD700",  # gold
    "#FF0000",  # Red
    "#008000",  # Green
    "#0000FF",  # Blue
    "#FFFF00",  # Yellow
    "#FFA500",  # Orange
    "#FFC0CB"   # Pink
]

for num_side in range(3,10):
    angle = 360/num_side
    t.color(colors[num_side-3])
    for i in range(num_side):
        t.forward(100)
        t.right(angle)


# random walk
 
angles = [90, 180,270,360]
t.width(10)
for _ in range(100):
    t.setheading(random.choice(angles))
    t.color(random.choice(colors))
    t.forward(20)

# spirograph

t.speed(50)
for i in range(100):
    current_heading = t.heading()
    t.setheading(current_heading+10)
    t.circle(100)


#  hirst painting

t.hideturtle()
t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)
t.speed(50)

for j in range(1,100):
    t.pendown()
    t.dot(20, random.choice(colors))
    t.penup()
    t.forward(50)

    if j % 10 == 0:
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(500)
        t.right(90)
        t.right(90)

screen = Screen()
screen.exitonclick()