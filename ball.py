from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#e9ecef")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_sleep = 0.06  # velocidad de la bola

    def ball_move(self):
        x_cor = self.xcor() - self.x_move
        y_cor = self.ycor() - self.y_move
        self.goto(x_cor, y_cor)

    def collision_wall(self):
        self.x_move *= -1

    def collision_ceiling(self):
        self.y_move *= -1

    def collision_paddle(self):
        self.y_move *= -1

    def collision_brick(self):
        self.y_move *= -1

    def new_level(self):
        self.ball_sleep *= 0.9
