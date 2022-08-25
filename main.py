# TODO: player bar (moving to left and right)
# TODO: ball
# TODO: hit bars
# TODO: score
# TODO: start menu

# -------------------------
from turtle import Screen

screen = Screen()
screen.setup(800, 600)
screen.title('Breakout')
screen.tracer(0)

is_on = True

while is_on:
    screen.update()

screen.exitonclick()
