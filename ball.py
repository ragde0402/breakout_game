import math
import turtle
import random


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(0, -240)
        self.xmove = random.uniform(-1, 1)
        self.ymove = abs(1 / self.xmove)
        if self.ymove > 2:
            self.ymove = 2

    def move(self):
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)

    def detect_collision_brick(self, brick):
        if brick.isvisible():
            if (brick.edges["bottom"] - 15 <= self.ycor() <= brick.edges["top"]
                and brick.edges["right"] >= self.xcor() >= brick.edges["left"]) \
                    or (brick.edges["top"] + 15 > self.ycor() >= brick.edges["bottom"]
                        and brick.edges["right"] >= self.xcor() >= brick.edges["left"]):
                self.ymove *= -1
                brick.hideturtle()
                return True
            elif (brick.edges["right"] + 15 > self.xcor() > brick.edges["left"]
                  and brick.edges["top"] >= self.ycor() >= brick.edges["bottom"]) \
                    or (brick.edges["left"] - 15 < self.xcor() < brick.edges["right"]
                        and brick.edges["top"] >= self.ycor() >= brick.edges["bottom"]):
                self.xmove *= -1
                brick.hideturtle()
                return True

    def detect_wall(self):
        if self.xcor() >= 490 or self.xcor() <= -490:
            self.xmove *= -1
            self.move()
        elif self.ycor() >= 290:
            self.ymove *= -1
            self.move()
        elif self.ycor() <= -290:
            return True

    def detect_padle(self, paddle):
        if paddle.edge["right"] >= self.xcor() >= paddle.edge["left"] \
                and paddle.edge["top"] >= self.ycor() >= paddle.edge["top"] - 5:
            angle = -(self.distance(x=600.0, y=-250) - paddle.distance(x=600.0, y=-250))
            if angle > 0:
                self.xmove = math.log(angle, 15)
                self.ymove = abs(1 / self.xmove)
                if self.ymove > 2:
                    self.ymove = 2
            elif angle < 0:
                self.xmove = 0 - math.log(abs(angle), 15)
                self.ymove = abs(1 / self.xmove)
                if self.ymove > 2:
                    self.ymove = 2

    def ball_reset(self):
        self.goto(0, -240)
        self.xmove = random.uniform(-1, 1)
        self.ymove = abs(1 / self.xmove)
        if self.ymove > 2:
            self.ymove = 2
