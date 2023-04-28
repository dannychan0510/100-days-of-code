from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create snake, food, and scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keyboard input
screen.listen()
# Assign keys to snake direction changes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Initialize game loop
game_is_on = True

while game_is_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Control the speed of the game

    snake.move()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new position
        snake.extend()  # Add a new segment to the snake
        scoreboard.increase_score()  # Update the scoreboard

    # Detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_is_on = False
        scoreboard.game_over()  # Display "Game Over" message

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()  # Display "Game Over" message

# Keep the screen open until it's clicked
screen.exitonclick()
