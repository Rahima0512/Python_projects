from turtle import Turtle
snake_pos = [(0, 0), (-20, 0), (-40, 0)]
Move_distance=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for s in snake_pos:
            self.add_segment(s)

    def add_segment(self,position):
        s1 = Turtle()
        s1.shape("square")
        s1.color("forestgreen")
        s1.penup()
        s1.goto(position)
        self.segments.append(s1)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start=len(self.segments)-1,end = 0,steps = -1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(Move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            (self.head).setheading(90)

    def down(self):
        if self.head.heading() != UP:
            (self.head).setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            (self.head).setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            (self.head).setheading(180)
