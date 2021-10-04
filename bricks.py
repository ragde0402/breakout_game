import turtle


class Brick(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("green")
        self.point = 1
        self.edges = {}
