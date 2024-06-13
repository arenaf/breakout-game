from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Briks
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=650, width=930)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0) # desactiva la animación de pantalla para que los segmentos se vean todos juntos

scoreboard = Scoreboard()
bricks = Briks()
all_bricks = bricks.total_bricks()
paddle = Paddle((0, -300))
ball = Ball()
screen.update()

# Movimiento de la pala con teclado
screen.listen()
screen.onkey(fun=paddle.go_to_left, key="Left")
screen.onkey(fun=paddle.go_to_right, key="Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_sleep)
    screen.update()
    ball.ball_move()

    # Detecta colisión con la pared
    if ball.xcor() > 450 or ball.xcor() < -450:
        ball.collision_wall()

    # Detecta colisión con el techo
    if ball.ycor() > 315:
        ball.collision_ceiling()

    # Detecta colisión con la pala
    if ball.distance(paddle) < 50 and ball.ycor() < -275:
        ball.collision_paddle()

    if ball.ycor() < -330:
        scoreboard.game_over()
        game_is_on = False

    # Elimina el bloque contra el que colisionó
    for one_brick in all_bricks:
        if ball.distance(one_brick) < 30:
            all_bricks.remove(one_brick)
            one_brick.reset()
            ball.collision_brick()
            scoreboard.new_score()

    # Sube de nivel
    if all_bricks == []:
        ball.new_level()
        bricks = Briks()
        all_bricks = bricks.total_bricks()
        scoreboard.new_level()


screen.exitonclick()
