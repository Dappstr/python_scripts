import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.speed("fastest")

screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


for i in range(int(360 / 5)):
    timmy.color(random_color())
    timmy.setheading(timmy.heading() + 5)
    timmy.circle(100)

screen.exitonclick()