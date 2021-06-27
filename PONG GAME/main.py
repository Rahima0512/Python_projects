import time
from turtle import Turtle,Screen
from Paddle import Paddle
from ball import Ball
from scores import ScoreBoard
screen=Screen()
#CREATED A SCREEN
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)
#CREATED A PADDLE
r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
#CREATED A SCORE OBJECT
scoreboard=ScoreBoard()

#CREATED A BALL OBJECT
ball=Ball()

screen.listen()
screen.onkey(r_paddle.goto_up, "Up")
screen.onkey(r_paddle.goto_down,"Down")
screen.onkey(l_paddle.goto_up, "w")
screen.onkey(l_paddle.goto_down,"s")






game_is_on=True
while game_is_on:
    if screen.onkey(scoreboard.game_over, "e"):
        exit()

    time.sleep(0.1)
    ball.move()
    #DETECTED COLLISION WITH WALL
    if ball.ycor() > 280 or ball.ycor() < (-280):
        ball.bounce_y()
    #DETECTED COLLISION WITH PADDLE
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()
        ball.speedy()

    if ball.xcor() > 380:
        ball.reset("right")
        scoreboard.l_score_update()

    if ball.xcor() < - 380:
        ball.reset("left")
        scoreboard.r_score_update()







    screen.update()



screen.exitonclick()