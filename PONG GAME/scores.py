from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.FONT=("Courier", 24, "bold")
        self.update_scoreboard()
    def update_scoreboard(self):
        self.goto(-150,250)
        self.write(f"{self.l_score}", False, align="left", font=self.FONT)
        self.goto(150,250)
        self.write(f"{self.r_score}", False, align="right", font=self.FONT)

    def l_score_update(self):
        self.l_score += 5
        self.clear()
        self.update_scoreboard()

    def r_score_update(self):
        self.r_score += 5
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,30)
        winner=max(self.l_score,self.r_score)
        self.write(f"Winner is    {winner}", False, align="center", font=self.FONT)
        self.goto(0,0)
        self.write(f"*****GAME OVER*****", False, align="center", font=self.FONT)
