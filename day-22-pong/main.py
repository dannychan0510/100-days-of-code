from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create a paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create a ball
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard()

# Listen for keyboard input
screen.listen()

# Assign keys to move paddle
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "q")
screen.onkeypress(l_paddle.down, "a")

# Initialize game loop
game_is_on = True

while game_is_on:

    # Update ball.prev_y before moving the ball
    ball.prev_x = ball.xcor()

    # Move ball
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.collide_with_wall():
        ball.bounce_y()

    # Detect collision with paddle
    if ball.collide_with_paddle(l_paddle) or ball.collide_with_paddle(r_paddle):
        ball.bounce_x()
        ball.increase_move_speed()

    # Detect if ball is out of bounds on the right side
    if ball.r_out_of_bounds():
        scoreboard.l_point()
        ball.reset_ball()

    # Detect if ball is out of bounds on the left side
    if ball.l_out_of_bounds():
        scoreboard.r_point()
        ball.reset_ball()

# Set screen to exit only on click
screen.exitonclick()
