from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard(self.score)

    def update_scoreboard(self, score):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level {score}", align="center", font=FONT)

    def lvl_up(self):
        self.score += 1
        self.update_scoreboard(self.score)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
