from tracemalloc import start
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

score = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game on Nokia 3310")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

def game_over():
    global game_is_on
    game_is_on = False
    print(f"Your score is: {score.score}!")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_over()

screen.exitonclick()
