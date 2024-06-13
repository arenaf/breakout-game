from turtle import Turtle

MOVE_DISTANCE = 30

class Paddle(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.color("#0079FF")
        self.goto(cords)

    # def up(self):
    #     new_y = self.ycor() + MOVE_DISTANCE
    #     self.goto(self.xcor(), new_y)
    #
    # def down(self):
    #     new_y = self.ycor() - MOVE_DISTANCE
    #     self.goto(self.xcor(), new_y)

    def go_to_left(self):
        if self.xcor() > -420:
            self.forward(-MOVE_DISTANCE)

    def go_to_right(self):
        if self.xcor() < 400:
            self.forward(MOVE_DISTANCE)