from turtle import Turtle,Screen
import random
#another method to importing is
#from turtle as t
#then we can do timmy = t.Turtle()

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")

colors = ["red", "blue", "green", "yellow", "magenta", "brown", "black", "indigo", "lime", "slate gray"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for sides in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(sides)


screen.exitonclick()