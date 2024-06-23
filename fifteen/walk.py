from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

def random_color():
    screen.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

timmy.shape("turtle")

turn = [90, 180, 270, 360]

timmy.pensize(10)
timmy.speed(8)
for i in range(0,50):
    timmy.color(random_color())
    timmy.right(random.choice(turn))
    timmy.forward(50)

screen.exitonclick()