import turtle as t

tim = t.Turtle()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t.bgcolor('black')
t.speed(10)
for x in range(360):
    tim.pencolor(colors[x % 6])
    tim.width(int(x / 100 + 1))
    tim.forward(x)
    tim.left(59)

screen = t.Screen()
screen.exitonclick()
