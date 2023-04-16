import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(7)
timmy.speed(5)

color_list = [
    "#72A1E5",  # Sky Blue
    "#9FE2BF",  # Seafoam Green
    "#FFD700",  # Gold
    "#F2A68F",  # Coral
    "#A8C3D8",  # Powder Blue
    "#E0E6F1",  # Light Grayish Blue
    "#B4D7BF",  # Sage Green
    "#E2B6C2",  # Soft Pink
    "#FFC1A1",  # Apricot
    "#D5C7E8",  # Lilac
    "#C5E3BF",  # Mint Green
    "#E8D1C2",  # Peach
]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# # Draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# # Draw a dashed line
# for _ in range(25):
#     timmy.pd()
#     timmy.forward(5)
#     timmy.pu()
#     timmy.forward(5)

# # Draw multiple shapes
# i = 0
# for n in range(3, 15):
#     timmy.color(random.choice(color_list))
#     i += 1
#     sides = n
#     turn_angle = 360 / sides
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(turn_angle)


# # Draw a random walk
# directions = [0, 90, 180, 270]
# for _ in range(1000):
#     timmy.color(random.choice(color_list))
#     timmy.setheading(random.choice(directions))
#     timmy.forward(25)


# # Above, but now with random colors
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
#
# directions = [0, 90, 180, 270]
# for _ in range(100):
#     timmy.color(random_color())
#     timmy.setheading(random.choice(directions))
#     timmy.forward(25)


# Spirograph exercise
def draw_spirograph(n):
    timmy.pensize(1)
    timmy.speed("fastest")
    tilt = 360 / n
    for _ in range(n):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.right(tilt)

draw_spirograph(30)

screen = t.Screen()
screen.exitonclick()