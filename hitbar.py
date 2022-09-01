from turtle import Turtle

#Create a list comprehension here later, with lines and columns
POSITIONS = [(-300, 250), (-230, 250), (-160, 250), (-90, 250), (-20, 250), (50, 250), (120, 250), (190, 250), (260, 250), (330, 250)]

class HitBar(Turtle):
    def __init__(self):
        self.bars = []

    def new_bar(self, position):
        new_bar = Turtle('square')
        new_bar.up()
        new_bar.shapesize(1, 3)
        new_bar.goto(position)
        self.bars.append(new_bar)
    
    def create_bars(self):
        for position in POSITIONS:
            self.new_bar(position)

    def remove_bar(self, bar):
        self.bars.remove(bar)