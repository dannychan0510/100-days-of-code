from turtle import Screen, Turtle
from snake import Snake
import time

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Creating a snake body
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# Setting screen to exit on click only
screen.exitonclick()
