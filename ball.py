from turtle import Turtle



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_sleep = 0.1  # velocidad de la bola

    def ball_move(self):
        x_cor = self.xcor() - self.x_move
        y_cor = self.ycor() - self.y_move
        self.goto(x_cor, y_cor)

    def reset_position(self):
        self.goto(0,-10)
        self.collision_paddle() # cambia la orientación de la bola hacia el otro jugador
        self.ball_sleep = 0.1

    def collision_wall(self):
        self.x_move *= -1

    def collision_ceiling(self):
        self.y_move *= -1
    def collision_paddle(self):
        self.y_move *= -1
        # self.ball_sleep *= 0.9

    def collision_brick(self):
        self.y_move *= 1
        # self.ball_sleep *= 0.9