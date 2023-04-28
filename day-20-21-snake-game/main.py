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
food = Food(snake)
scoreboard = Scoreboard()
last_key_press_time = 0  # Store the time of the last key press

# Define a wrapper function to handle key press events
def on_key_press(func):
    global last_key_press_time
    current_time = time.time()

    # Check if the time since the last key press is greater than 0.1 seconds
    if current_time - last_key_press_time > 0.1:
        func()
        last_key_press_time = current_time


# Listen for keyboard input
screen.listen()
# Assign keys to snake direction changes with the on_key_press wrapper function
screen.onkey(lambda: on_key_press(snake.up), "Up")
screen.onkey(lambda: on_key_press(snake.down), "Down")
screen.onkey(lambda: on_key_press(snake.left), "Left")
screen.onkey(lambda: on_key_press(snake.right), "Right")

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
