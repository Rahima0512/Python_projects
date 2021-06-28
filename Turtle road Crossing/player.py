from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("forestgreen")
        self.setheading(90)
        self.reset_turtle()

    def reset_turtle(self):
        self.goto(STARTING_POSITION)
    def move(self):
        self.forward(MOVE_DISTANCE)
    def is_at_finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True

