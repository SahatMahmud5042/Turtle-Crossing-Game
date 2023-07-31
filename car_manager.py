from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def gen_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.new_y = random.randint(-240, 240)
            new_car.goto(300, new_car.new_y)
            self.all_cars.append(new_car)

    def car_move(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def move_incr(self):
        self.car_speed = self.car_speed + MOVE_INCREMENT

