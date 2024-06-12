from turtle import Turtle


class Briks(Turtle):
    def __init__(self):
        super().__init__()
        self.init_board()
        self.hideturtle()

    def put_bricks(self, new_turtle, coordx, coordy, color):
        new_turtle.shape("square")
        new_turtle.shapesize(stretch_wid=1, stretch_len=3)
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto((coordx, coordy))

    def init_board(self):
        coordy = 30
        color = ["yellow", "yellow", "green", "green", "orange", "orange", "red", "red"]
        # color = ["#F5DD61", "#F5DD61", "#9ADE7B", "#9ADE7B", "#FF6D60", "#FF6D60", "#D61355", "#D61355"]
        # color = ["#FCE22A", "#FCE22A", "#81B214", "#81B214", "#F94A29", "#F94A29", "#D61355", "#D61355"]
        for i in range(8):
            coordx = -425
            for _ in range(14):
                bricks = Turtle()
                self.put_bricks(bricks, coordx, coordy, color[i])
                coordx += 65
            coordy += 30


if __name__ == "__main__":
    bricks = Briks()
