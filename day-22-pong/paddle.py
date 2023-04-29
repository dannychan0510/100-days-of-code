from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")  # Set the color of the segment to white
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()  # Lift the pen to prevent drawing
        self.setposition(position)  # Set the position of the segment

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
