import random
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


tim.pensize(10)
tim.speed(6)
heading = [0, 90, 180, 270]
for _ in range(400):
    tim.color(random_color())
    tim.setheading(random.choice(heading))
    tim.fd(20)


screen = t.Screen()
screen.exitonclick()
