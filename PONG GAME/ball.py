from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.goto(0,0)
        self.x_new=10
        self.y_new=10
        self.boost = 0
    def move(self):
        new_x=self.xcor()+self.x_new
        new_y=self.ycor()+self.y_new
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_new*=-1
    def bounce_x(self):
        self.x_new*=-1
    def reset(self,miss):
        self.goto(0, 0)
        if(miss=='right'):
            self.bounce_x()
        if (miss == 'left'):
            self.bounce_y()
    def speedy(self):
        self.boost+=1
        if self.boost >10:
            self.boost=0
        self.speed(self.boost)


