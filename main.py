from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Briks
import time

# Pingpong
# Turtle crossing game


screen = Screen()
screen.setup(height=650, width=930)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0) # desactiva la animación de pantalla para que los segmentos se vean todos juntos

ball = Ball()
bricks = Briks()
paddle = Paddle((0, -300))
screen.update()


# Movimiento de la pala
screen.listen()
screen.onkey(fun=paddle.go_to_left, key="Left")
screen.onkey(fun=paddle.go_to_right, key="Right")
# screen.update()


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_sleep)
    screen.update()
    ball.ball_move()

    # Detected collision with walls
    if ball.xcor() > 450 or ball.xcor() < -450:
        ball.collision_wall()

    # Detected collision with ceiling
    if ball.ycor() > 315:
        ball.collision_ceiling()

    # Detected collision with paddle
    if (ball.distance(paddle) < 50 and ball.xcor() > -465) or (ball.distance(paddle) < 50 and ball.xcor() > 465):
        ball.collision_paddle()

    if ball.distance(bricks) < 20:
        print("Collision brick")
        ball.collision_brick()



screen.exitonclick()
