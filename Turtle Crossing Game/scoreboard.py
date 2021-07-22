from turtle import Turtle

FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(-210, 260)
        self.level = 1
        self.print_level()

    def print_level(self):
        """prints game level on the screen"""
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def level_up(self):
        """Increases game level"""
        self.level += 1
        self.clear()
        self.print_level()

    def game_over(self):
        """Prints game over on the screen"""
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=FONT)
