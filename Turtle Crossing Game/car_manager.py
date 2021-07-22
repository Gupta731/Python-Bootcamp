from turtle import Turtle
import random

COLORS = ["firebrick2", "orange", "yellow", "green", "royalblue", "purple", "orchid", "aquamarine2"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 0.1
        self.initial_cars()

    def initial_cars(self):
        """Adds initial few cars on the screen"""
        for car in range(10):
            new_car = Turtle('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(random.randrange(-200, 200, 50), random.randrange(-250, 250, 30))
            self.all_cars.append(new_car)

    def create_car(self):
        """Adds new cars"""
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            new_car = Turtle('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(random.randrange(300, 350, 50), random.randrange(-250, 250, 30))
            self.all_cars.append(new_car)

    def move(self):
        """Moves the cars across the screen"""
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def speed_level_up(self):
        """Speeds up the car"""
        self.car_speed *= 0.5
