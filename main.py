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
all_bricks = bricks.total_bricks()

# Movimiento de la pala
screen.listen()
screen.onkey(fun=paddle.go_to_left, key="Left")
screen.onkey(fun=paddle.go_to_right, key="Right")
# screen.update()
cont = 0

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
    if ball.distance(paddle) < 50 and ball.ycor() < -275:
        ball.collision_paddle()

    # Elimina el bloque contra el que colisionó
    for one_brick in all_bricks:
        if ball.distance(one_brick) < 30:
            print(one_brick)
            print("Collision brick", cont)
            cont += 1
            all_bricks.remove(one_brick)
            one_brick.reset()
            print(len(all_bricks))
            ball.collision_brick()


screen.exitonclick()
