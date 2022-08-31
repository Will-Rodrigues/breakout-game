from turtle import Turtle


class PlayerBar(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape('square')
        self.shapesize(1, 5)
        self.goto(0, -250)

    def move_left(self):
        if self.xcor() > -340:
            self.setx(self.xcor() - 20)

    def move_right(self):
        if self.xcor() < 340:
            self.setx(self.xcor() + 20)
