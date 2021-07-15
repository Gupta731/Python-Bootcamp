from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput('Make your bet', 'Which turtle will win the race? Enter a colour: ')
colours = ['Red', 'Orange', 'Yellow', 'DarkOrchid3', 'Blue', 'aquamarine3']
y_positions = [-80, -40, 0, 40, 80, 120]
turtle_family = []

is_race_on = False
if user_bet in colours:
    is_race_on = True
else:
    is_race_on = False
    print('Please enter correct bet.')

for turtle in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colours[turtle])
    new_turtle.goto(-235, y_positions[turtle])
    turtle_family.append(new_turtle)


while is_race_on:
    for turtle in turtle_family:
        turtle.speed(3)
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f'You won. Winning Turtle is {turtle.pencolor()}')
            else:
                print(f'You lose. Winning Turtle is {turtle.pencolor()}')
            break
screen.exitonclick()
