from turtle import Turtle
import random

START_POS = (random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.goto(START_POS)

    def jump(self):
        new_pos = (random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))

        self.goto(new_pos)
        