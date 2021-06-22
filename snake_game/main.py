import time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
scores=0
snake=Snake()
food=Food()
scoreboard=ScoreBoard()

screen=Screen()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake Game")
screen.tracer(0)

is_game_on=True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    #DETECT COLLISION WITH FOOD

    if(snake.head.distance(food)<15):
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # DETECT COLLISION WITH WALL

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_game_on=False

    # DETECT COLLISION WITH TAIL
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            scoreboard.game_over()
            is_game_on = False







screen.exitonclick()