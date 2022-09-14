from turtle import Turtle
FONT = ('Courier', 20, 'bold')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto((0, 280))
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", font=FONT, align=ALIGNMENT)
