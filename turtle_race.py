import random
from turtle import Turtle,Screen
colour=["red","yellow","coral","pink","black","blue"]
turtle_gang=[]
count=0
y_pos=-150
is_game_on=False
for tim in range(0,6):
    evry_turtle=Turtle("turtle")
    evry_turtle.color(colour[tim])
    count=count+1
    evry_turtle.penup()
    evry_turtle.speed()
    evry_turtle.goto(x=-230,y=y_pos)
    y_pos+=50
    turtle_gang.append(evry_turtle)



screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Welcome to the turtle match",prompt="Enter the colour of the turtle you want to bet on")
print(user_bet)
if user_bet:
    is_game_on=True

while(is_game_on==True):

    for tim in turtle_gang:
        if tim.xcor()>230:
            is_game_on=False
            winner=tim.pencolor()
            if winner==user_bet:
                print(f"You Won!!!!!!!!! {winner} has won the race")
            else:
                print(f"You Lose!!!!!!!!! {winner} has won the race")

        random_distance = random.randint(0, 10)
        tim.forward(random_distance)

screen.exitonclick()