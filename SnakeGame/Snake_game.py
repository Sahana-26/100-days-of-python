from turtle import *

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for seg in range(len(self.segments)-1,0,-1):
            x_cor = self.segments[seg-1].xcor()
            y_cor = self.segments[seg-1].ycor()
            self.segments[seg].goto(x_cor,y_cor)

        self.head.forward(20)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)
            
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)
