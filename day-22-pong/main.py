from turtle import Screen
from paddle import Paddle
from ball import Ball
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
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.collide_with_paddle(l_paddle) or ball.collide_with_paddle(r_paddle):
        ball.bounce_x()

# Set screen to exit only on click
screen.exitonclick()
