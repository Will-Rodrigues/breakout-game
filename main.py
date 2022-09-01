# TODO: hit bars
# TODO: score
# TODO: start menu

# -------------------------
from turtle import Screen
from bar import PlayerBar
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.title('Breakout')
screen.tracer(0)

player = PlayerBar()
ball = Ball()

is_on = True

screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(ball.release, "space")

while is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() < -280:
        ball.reset_position()

    elif ball.xcor() < -375 or ball.xcor() > 375:
        ball.hit_sides()
    
    if ball.x_move != 0:
        if ball.distance(player) < 25 or ball.ycor() > 250:
            ball.hit_up_down()

screen.exitonclick()
