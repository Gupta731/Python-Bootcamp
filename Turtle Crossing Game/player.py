from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__('turtle')
        self.penup()
        self.color('white')
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def turtle_up(self):
        """Moves the turtle upwards"""
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def reset_player(self):
        """Resets turtle position when it reaches finish line"""
        self.goto(STARTING_POSITION)
