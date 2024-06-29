from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score_board

import time
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

score_board = Score_board()

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()

screen.listen()

def move_up(paddle):
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)
def move_down(paddle):
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)

screen.onkey(lambda: move_up(left_paddle), "w")
screen.onkey(lambda: move_up(right_paddle), "Up")
screen.onkey(lambda: move_down(left_paddle), "s")
screen.onkey(lambda: move_down(right_paddle), "Down")

game_running = True
while game_running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_move *= -1

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.x_move *= -1
        ball.move_speed *= 0.9

    # Detect when ball goes beyond paddles
    if ball.xcor() > 400 or ball.xcor() < -400:
        # Right paddle
        if ball.xcor() > 400:
            ball.x_move *= -1
            ball.goto(0,0)
            score_board.l_score += 1
            score_board.update_scoreboard()
            ball.move_speed = 0.1

        # Left paddle
        elif ball.xcor() < -400:
            ball.x_move *= -1
            ball.goto(0,0)
            score_board.r_score += 1
            score_board.update_scoreboard()
            ball.move_speed = 0.1



screen.exitonclick()