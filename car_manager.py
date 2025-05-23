from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def increase_level(self):
        self.move_distance += MOVE_INCREMENT
