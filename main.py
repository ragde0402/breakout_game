import turtle
import random
from bricks import Brick
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, GameOver
import time

game_is_on = True


def create_bricks(color: str, position: int):
    """

    :param color: color of bricks
    :param position: line of bricks (counting from down to top)
    :return: full line of bricks in specified color and position (counting from down to top)
    """
    start = -500
    for x in range(40):
        if start < 480:
            stretch = random.randrange(1, 4, 1)
            start += stretch * 10 + 5
            brick_one = Brick()
            brick_one.color(color)
            brick_one.goto(start, 30 * position + 10)
            brick_one.point = position
            brick_one.shapesize(1, stretch)
            start += stretch * 10 + 5
            brick_one.edges = {"left": brick_one.xcor() - stretch * 10, "right": brick_one.xcor() + stretch * 10,
                               "top": brick_one.ycor() + 10, "bottom": brick_one.ycor() - 10}
            all_bricks.append(brick_one)


screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("Breakout")
screen.tracer(0)
screen.listen()

paddle = Paddle()
ball = Ball()

screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

while game_is_on:
    scoreboard = Scoreboard()

    all_bricks = []
    if len(all_bricks) == 0:
        create_bricks("green", 1)
        create_bricks("blue", 2)
        create_bricks("yellow", 3)
        create_bricks("red", 4)
        while len(all_bricks) > 0 and game_is_on:
            ball.move()
            ball.detect_padle(paddle)
            for brick in all_bricks:
                if ball.detect_collision_brick(brick):
                    all_bricks.remove(brick)
                    point = brick.point
                    scoreboard.points += point
                    scoreboard.update_scoreboard()
            if ball.detect_wall():
                scoreboard.lives -= 1
                scoreboard.update_scoreboard()
                if scoreboard.lives == 0:
                    game_is_on = False
                    game_over = GameOver()
                    game_over.game_over()
                time.sleep(1)
                ball.ball_reset()
            screen.update()

screen.exitonclick()
