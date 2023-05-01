from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)

            random_starting_y = random.randint(-250, 250)
            new_car.setposition(300, random_starting_y)

            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.move_speed
            car.goto(new_x, car.ycor())

    def collision(self, turtle):
        for car in self.all_cars:
            if car.xcor() - 25 <= turtle.xcor() <= car.xcor() + 25 \
                    and car.ycor() - 20 <= turtle.ycor() <= car.ycor() + 20:
                return True

    def increase_move_speed(self):
        self.move_speed += MOVE_INCREMENT
