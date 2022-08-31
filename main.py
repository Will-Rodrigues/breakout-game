# TODO: ball
# TODO: hit bars
# TODO: score
# TODO: start menu

# -------------------------
from turtle import Screen
from bar import PlayerBar

screen = Screen()
screen.setup(800, 600)
screen.title('Breakout')
screen.tracer(0)

player = PlayerBar()

is_on = True

screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

while is_on:
    screen.update()

screen.exitonclick()
