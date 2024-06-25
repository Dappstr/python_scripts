from turtle import Turtle, Screen
import random

is_race_going = False

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
all_turtles = []

user_bet = screen.textinput("Pick a turtle", "Which color do you think will win?")

for turtle_indexs in range(0, 6):
    timmy = Turtle(shape = "turtle")
    timmy.color(colors[turtle_indexs ])
    timmy.penup()
    timmy.goto(x=-240, y = (turtle_indexs + 1) * 30)
    all_turtles.append(timmy)

if user_bet:
    is_race_going = True

while is_race_going:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_going = False
            if turtle.pencolor() == user_bet:
                print("You won!")
            else:
                print("You lost. The winning color was: " + turtle.pencolor())
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()