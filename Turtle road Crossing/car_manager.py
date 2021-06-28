from turtle import Turtle, shapesize
import random

COLORS = ["red", "orange", "yellow", "white", "blue", "purple","coral","pink","grey"]



class CarManager:
    def __init__(self):

        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 5
        self.all_cars=[]
        self.car_speed=self.MOVE_INCREMENT

    def car_maker(self):
        chance=random.randint(1,6)
        if chance==6:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.speed(0.1)
            car.color(random.choice(COLORS))
            car.goto(280, random.randint(-250, 250))
            self.all_cars.append(car)


    def car_mover(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed+=self.MOVE_INCREMENT









