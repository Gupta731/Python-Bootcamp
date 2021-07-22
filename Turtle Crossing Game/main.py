import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.turtle_up, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(cars.car_speed)
    screen.update()

    cars.create_car()
    cars.move()

    # Detect when turtle reaches finish line
    if player.ycor() >= 280:
        score.level_up()
        player.reset_player()
        cars.speed_level_up()

    # detect when turtle collides with a car
    for car in cars.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            score.game_over()

screen.exitonclick()
