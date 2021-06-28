import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

"""       TURTLE CROSSING
1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. 
On the next level, the car speed increases.
4. When the turtle collides with a car, it's game over and everything stops.
    """
screen = Screen()


screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Turtle vs. Traffic")
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_maker()
    car_manager.car_mover()
    #Detect collision:
    for car in car_manager.all_cars:
        if player.distance(car)<20:
            scoreboard.game_over()
            game_is_on=False
    #Detect successful crossing:
    if player.is_at_finish_line():

        scoreboard.level_update()
        player.reset_turtle()
        car_manager.level_up()
        time.sleep(0.8)


screen.exitonclick()