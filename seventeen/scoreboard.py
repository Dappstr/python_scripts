from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 24, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=("Arial", 24, "normal"))
