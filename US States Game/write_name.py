from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 8, 'normal')


class WriteName(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def writer(self, state, xcor, ycor):
        self.goto(xcor, ycor)
        self.write(f'{state}', align=ALIGNMENT, font=FONT)
