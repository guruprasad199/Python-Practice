import turtle

t = turtle.Turtle()
screen = turtle.getscreen()
screen.bgcolor("black")
t.speed(0)

colors = ["white", "magenta", "blue"]

for i in range(50):
    for color in colors:
        t.color(color)
        t.pensize(5)
        t.left(12)
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)

turtle.done()