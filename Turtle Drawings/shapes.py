import random
from turtle import Turtle, Screen
t = Turtle()
colors = ['aquamarine', 'chocolate', 'chartreuse3', 'coral2', 'maroon2', 'yellow1', 'violet']

for i in range(3, 11):
    t.color(random.choice(colors))
    for _ in range(i):
        t.fd(100)
        t.right(360/i)

screen = Screen()
screen.exitonclick()
