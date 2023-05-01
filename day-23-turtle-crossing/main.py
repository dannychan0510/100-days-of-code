import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialise player
player = Player()

# Initialise CarManager object
car_manager = CarManager()

# Initialise scoreboard
scoreboard = Scoreboard()

# Initialise loop and level counter
loop_n = 0
level = 1

# Set up controls
screen.listen()
screen.onkey(player.move_up, "Up")

# Initialise game
game_is_on = True
while game_is_on:

    # Game speed adjustment and update screen
    time.sleep(0.1)
    screen.update()

    # Generate a new car every 6th loop
    car_manager.create_car()

    # Move cars forward
    car_manager.move_cars()

    # For each car, detect whether it has collided with player
    if car_manager.collision(player):
        game_is_on = False
        scoreboard.game_over()

    # Increase speed, level, update scoreboard, and reset if player reaches finish
    if player.has_reach_finish_line():
        player.reset_position()
        car_manager.increase_move_speed()
        scoreboard.level_up()
        scoreboard.update_scoreboard()
        time.sleep(0.75)

# Exit screen only on click
screen.exitonclick()
