import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


for _ in range(int(360/5)):
    tim.color(random_color())
    tim.circle(90)
    tim.left(5)


screen = t.Screen()
screen.exitonclick()
