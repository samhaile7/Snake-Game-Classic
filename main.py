from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Sam Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food.xcor(), food.ycor()) <= 15:
        food.jump()
        scoreboard.increase_score()
        snake.extend()
        snake.extend()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment.xcor(), segment.ycor()) < 10:
            snake.reset()
            scoreboard.reset()

screen.exitonclick()
