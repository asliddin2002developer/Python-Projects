from turtle import Screen

import score_board
from snake import Snake
from food import Food
from score_board import ScoreBoard

import time


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("yellow")
screen.title("My Snake Game.")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #Detect the collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.make_snake_bigger()
        scoreboard.speed(0)
        scoreboard.change_score()
        screen.update()



    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        scoreboard.reset()
        snake.reset_snake()
        snake.create_snake()
        # else:
        #     game_is_on = False

    #Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()
            # else:
            #     game_is_on = False



screen.exitonclick()