from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.Level=1
        self.color("white")
        self.goto(-150,270)
        self.scores()

    def scores(self):
        self.write(f"Level - {self.Level}",False,"center",font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(f"****** GAME OVER *****", False, "center", font=("Courier", 20, "bold"))
        self.goto(0, -30)
        self.write(f"At Level - {self.Level}", False, "center", font=("Courier", 20, "bold"))
    def level_update(self):
        self.Level=self.Level+1
        self.clear()
        self.scores()
