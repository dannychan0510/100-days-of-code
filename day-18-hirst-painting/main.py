import turtle as t
import colorgram
import random

# Extract color scheme from image.jpg
# colors = colorgram.extract("image.jpg", 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)

# Color list from colorgram
color_list = [(9, 101, 75), (27, 47, 37), (27, 47, 69), (39, 56, 108), (44, 38, 30), (49, 34, 45), (49, 158, 178),
              (53, 106, 136), (53, 122, 86), (74, 160, 121), (103, 120, 168), (113, 43, 33), (120, 35, 56),
              (120, 179, 153), (123, 162, 187), (143, 67, 93), (151, 85, 55), (155, 212, 188), (166, 151, 46),
              (198, 86, 117), (202, 131, 155), (216, 149, 90), (217, 86, 61), (220, 231, 239), (229, 201, 115),
              (231, 242, 236), (239, 161, 184), (244, 234, 224), (245, 167, 155), (245, 229, 235)]


def draw_hirst_painting(dot_size=20, spacing=50, padding=50):
    """
    Draw a Hirst-style painting using turtle graphics.

    This function uses the turtle graphics library to draw a Hirst-style painting
    consisting of a 10x10 grid of dots, with each dot being filled with a random color
    from a pre-defined list of colors. The dot size, spacing between dots, and padding
    around the canvas can be customized using the function arguments.

    Args:
        dot_size (int, optional): Size of each dot in pixels. Defaults to 20.
        spacing (int, optional): Spacing between dots in pixels. Defaults to 50.
        padding (int, optional): Padding around the canvas in pixels. Defaults to 50.

    Returns:
        None

    """
    # Set colormode
    t.colormode(255)

    # Create turtle object
    brush = t.Turtle()
    brush.hideturtle()
    brush.speed("fastest")
    brush.pu()

    # Set dot size, spacing, and padding variables
    canvas_width = (spacing * 9.5) + (padding * 2)
    canvas_height = (spacing * 9.5) + (padding * 2)
    starting_x = -(canvas_width/2) + (padding + (dot_size/2))
    starting_y = -(canvas_height/2) + (padding + (dot_size/2))

    # Set canvas size
    screen = t.Screen()
    screen.setup(width=canvas_width, height=canvas_height)

    # Set y_increment variable
    y_increment = 0

    # For each row
    for _ in range(10):

        # Set brush starting point
        brush.setx(starting_x)
        brush.sety(starting_y + y_increment)

        # Draw dot in each column, and move forward
        for _ in range(10):
            brush.dot(dot_size, random.choice(color_list))
            brush.forward(spacing)

        # After drawing dots, increment starting_y by spacing
        y_increment += spacing

    # Set screen to be exit on click
    screen.exitonclick()


# Call function
draw_hirst_painting(dot_size=20, spacing=50, padding=50)