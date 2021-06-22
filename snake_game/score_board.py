from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=268)
        self.score=0
        self.score_update()

    def score_update(self):
        self.write(f"Score  =  {self.score}", False, align="center", font=("Courier", 24, "normal"))
    def game_over(self):
        self.clear()
        self.goto(0,30)
        self.write(f"Final Score  =  {self.score}", False, align="center", font=("Courier", 24, "bold"))
        self.goto(0,0)
        self.write(f"*****GAME OVER*****", False, align="center", font=("Courier", 24, "bold"))


    def increase_score(self):
        self.score+=1
        self.clear()
        self.score_update()







