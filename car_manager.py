from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7


class CarManager:
    def __init__(self):
        self.cars = []
        self.counter = 0
        self.make_car()

    def make_car(self):
        y = random.randint(-240, 240)
        random_color = random.choice(COLORS)
        car = Turtle("square")
        car.penup()
        car.color(random_color)
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.setheading(180)
        car.goto(x=280, y=y)
        self.cars.append(car)

    def move_cars(self, lvl):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + lvl*MOVE_INCREMENT)

    def count_loop(self):
        self.counter += 1
