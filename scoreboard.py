from turtle import Turtle
FONT = ('Courier', 20, 'bold')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data_file:
            self.high_score = int(data_file.read())
        self.penup()
        self.goto((0, 280))
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", font=FONT, align=ALIGNMENT)

    def increase_score(self):

        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data_file:
                data_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

