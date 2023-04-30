import time
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.prev_x = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def collide_with_wall(self):
        if abs(self.ycor()) > 280:
            return True
        else:
            return False

    def collide_with_paddle(self, paddle):
        if paddle.xcor() - 20 <= self.xcor() <= paddle.xcor() + 20:
            if paddle.ycor() - 50 <= self.ycor() <= paddle.ycor() + 50:
                # Check if the ball is moving towards the paddle
                if (self.xcor() > self.prev_x) and (
                        paddle.xcor() > 0):  # Moving upwards and colliding with the right paddle
                    return True
                elif (self.xcor() < self.prev_x) and (
                        paddle.xcor() < 0):  # Moving downwards and colliding with the left paddle
                    return True
        else:
            return False

    def increase_move_speed(self):
        self.move_speed *= 0.9

    def r_out_of_bounds(self):
        if self.xcor() > 380:
            return True
        else:
            return False

    def l_out_of_bounds(self):
        if self.xcor() < -380:
            return True
        else:
            return False

    def reset_ball(self):
        self.setposition(0, 0)
        self.move_speed = 0.1
        self.screen.update()
        time.sleep(0.5)
        self.bounce_x()
