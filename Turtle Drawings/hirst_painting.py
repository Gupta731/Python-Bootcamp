import random
from turtle import Turtle, Screen
import colorgram

colors = colorgram.extract('hirst_sample.jpeg', 40)
rgb_colours = []
for item in colors:
    r = item.rgb.r
    g = item.rgb.g
    b = item.rgb.b
    if r < 230 and g < 230 and b < 230:
        color = (r, g, b)
        rgb_colours.append(color)
# print(rgb_colours)

# rgb_colours = [(195, 166, 108), (134, 167, 194), (47, 103, 147), (147, 89, 41), (189, 157, 32), (10, 21, 55),
#                (225, 209, 113), (63, 23, 9), (185, 141, 166), (68, 120, 79), (60, 12, 24), (137, 180, 150),
#                (137, 27, 11), (130, 76, 104), (14, 41, 25), (18, 52, 137), (125, 24, 40), (171, 99, 134),
#                (91, 153, 99), (175, 188, 218), (86, 120, 186), (21, 94, 65), (184, 98, 85), (211, 177, 201),
#                (66, 153, 170), (90, 78, 13), (167, 208, 177), (160, 204, 213), (13, 88, 105), (221, 179, 172)]

t = Turtle()
screen = Screen()
screen.colormode(255)
t.speed(0)
t.hideturtle()
t.penup()
t.setpos(-280, -250)
t.pendown()


def change_position():
    t.penup()
    t.setpos(-280, t.ycor()+40)
    t.pendown()


def draw_hirst():
    for _ in range(15):
        t.dot(18, random.choice(rgb_colours))
        t.penup()
        t.fd(40)
        t.pendown()


for _ in range(14):
    draw_hirst()
    change_position()


screen.exitonclick()
