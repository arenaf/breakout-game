from turtle import Turtle

FONT_LEVEL = ("Courier", 12, "bold")
FONT_SCORE = ("Courier", 25, "bold")
FONT_GAME_OVER = ("Courier", 50, "bold")
FONT_HIGH = ("Courier", 12, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.create_score()

    def create_score(self):
        self.penup()
        self.hideturtle()
        self.color("grey")
        self.update_score()

    def update_score(self):
        self.goto(450, 290)
        self.write(f"Level: {self.level}", align="right", font=FONT_LEVEL)
        self.goto(-430, 270)
        self.write(f"Score: {self.score}", align="left", font=FONT_SCORE)
        self.goto(430, 250)
        self.write(f"High Score: 0", align="right", font=FONT_HIGH)

    def new_score(self):
        self.score += 4
        self.clear()
        self.update_score()
        return self.score

    def new_level(self):
        self.level += 1
        self.clear()
        self.update_score()
        # return self.level


    def game_over(self):
        self.goto(0,-50)
        self.write(f"GAME OVER", align="Center", font=FONT_GAME_OVER)