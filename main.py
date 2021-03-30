from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

game_on = True
game_time = 0.1

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

while game_on:
    screen.update()
    time.sleep(game_time)
    snake.move()
    if snake.head.distance(food) < 15:
        food.change_location()
        snake.increase_part()
        scoreboard.increase_score()
    if snake.hit_wall():
        snake.reset_snake()
        scoreboard.reset_game()
    if snake.collides():
        snake.reset_snake()
        scoreboard.reset_game()

    screen.listen()
    screen.onkey(fun=snake.up, key='Up')
    screen.onkey(fun=snake.down, key='Down')
    screen.onkey(fun=snake.left, key='Left')
    screen.onkey(fun=snake.right, key='Right')

screen.exitonclick()
