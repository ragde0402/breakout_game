from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.points = 0
        self.lives = 5
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 200)
        self.write(f"Points: {self.points}", align="center", font=("Courier", 50, "normal"))
        self.goto(300, 200)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 50, "normal"))

    def point(self, n):
        self.points += n
        self.update_scoreboard()

    def live(self):
        self.lives -= 1
        self.update_scoreboard()


class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def game_over(self):
        self.goto(0, -100)
        self.write("Game Over.", align="center", font=("Courier", 30, "normal"))
