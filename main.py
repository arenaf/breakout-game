from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Briks
from scoreboard import Scoreboard
import time

# Pingpong
# Turtle crossing game


screen = Screen()
screen.setup(height=650, width=930)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0) # desactiva la animación de pantalla para que los segmentos se vean todos juntos

scoreboard = Scoreboard()
# score = scoreboard.create_score()
# level = scoreboard.create_level()
bricks = Briks()
all_bricks = bricks.total_bricks()
paddle = Paddle((0, -300))
ball = Ball()
screen.update()


# Movimiento de la pala
screen.listen()
screen.onkey(fun=paddle.go_to_left, key="Left")
screen.onkey(fun=paddle.go_to_right, key="Right")
# screen.update()
# cont = 0

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

    if ball.ycor() < -330:
        scoreboard.game_over()


    # Elimina el bloque contra el que colisionó
    for one_brick in all_bricks:
        if ball.distance(one_brick) < 30:
            # print("Collision brick", cont)
            # cont += 1
            all_bricks.remove(one_brick)
            one_brick.reset()
            ball.collision_brick()
            scoreboard.new_score()

    if all_bricks == []:
        ball.new_level()
        bricks = Briks()
        all_bricks = bricks.total_bricks()
        scoreboard.new_level()


screen.exitonclick()



# TODO 3: poder reiniciar partida
# TODO : data high score
