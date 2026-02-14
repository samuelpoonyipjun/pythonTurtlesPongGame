from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"Score:{self.l_score} : {self.r_score}", align="center", font=("Verdana", 15, "normal"))
    def increase_score_l(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
    def increase_score_r(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0, 0)
        if self.l_score == 5:
            self.write(f"Game over, player 1 won.", align="center", font=("Verdana", 15, "normal"))
        if self.r_score == 5:
            self.write(f"Game over, player 2 won.", align="center", font=("Verdana", 15, "normal"))