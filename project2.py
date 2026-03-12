'''
Ivan D. Linares
a house with a front lawn
'''

# loads the Turtle graphics module, which is a built-in library in Python
import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """Draw a curved line using small line segments"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        
    segment_length = length / segments
    original_heading = t.heading()
    
    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)
    
    t.setheading(original_heading)
    
    if fill_color:
        t.end_fill()
        
def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_house(t, x, y, size, wall_color="tan", roof_color="red", door_color="saddlebrown", window_color="lightblue"):
    """Draw a house at position (x, y) with given size and colors"""
    # house body
    jump_to(t, x, y)
    draw_square(t, size, wall_color)

    # roof
    jump_to(t, x, y)
    draw_triangle(t, size, roof_color)

    # door: compute width/height and position so it sits on the house base
    door_width = size // 5
    door_height = size * 2 // 5
    door_x = x + (size - door_width) // 2
    door_y = y - size + door_height
    jump_to(t, door_x, door_y)
    draw_rectangle(t, door_width, door_height, door_color)

    # windows: smaller squares positioned on the upper half of the house
    window_size = size // 6
    left_window_x = x + size // 6
    right_window_x = x + size - size // 6 - window_size
    window_top_y = y - size // 3
    jump_to(t, left_window_x, window_top_y)
    draw_square(t, window_size, window_color)
    jump_to(t, right_window_x, window_top_y)
    draw_square(t, window_size, window_color)


def draw_scene(t):
    """
    This scene is created by layering shapes from the background to the foreground
    using jump_to() for positioning and color-filled shapes for clarity.
    """
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    # lawn (top y coordinate used to align house bottoms)
    lawn_top = -90
    jump_to(t, -400, lawn_top)
    draw_rectangle(t, 800, 200, "green")

    # Draw multiple houses with different sizes and colors; align bottoms to lawn_top
    # two smaller houses on the left
    draw_house(t, -380, lawn_top + 70, 70, "lightgrey", "darkgrey", "sienna", "lightblue")
    draw_house(t, -300, lawn_top + 90, 90, "beige", "brown", "sienna", "lightblue")

    # existing houses
    draw_house(t, -200, lawn_top + 200, 200, "tan", "red", "saddlebrown", "lightblue")
    draw_house(t, 50, lawn_top + 150, 150, "lightyellow", "darkred", "brown", "lightblue")
    draw_house(t, 250, lawn_top + 120, 120, "lightcoral", "orange", "maroon", "lightblue")

    # sun
    jump_to(t, 250, 160)
    draw_circle(t, 80, "yellow")


def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()


if __name__ == "__main__":
    main()
