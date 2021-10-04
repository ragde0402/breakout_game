import turtle


class Paddle(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("grey")
        self.shapesize(stretch_wid=0.5, stretch_len=6)
        self.goto(0, -250)
        self.edge = {"left": self.xcor() - 60, "right": self.xcor() + 60, "top": self.ycor() + 10}

    def move_left(self):
        new_xcor = self.xcor() - 20
        self.goto(new_xcor, self.ycor())
        self.edge = {"left": new_xcor - 60, "right": new_xcor + 60, "top": self.ycor() + 10}

    def move_right(self):
        new_xcor = self.xcor() + 20
        self.goto(new_xcor, self.ycor())
        self.edge = {"left": new_xcor - 60, "right": new_xcor + 60, "top": self.ycor() + 10}
