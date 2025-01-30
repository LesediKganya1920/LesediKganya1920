import turtle

def draw_ring(radius):
    """Draw a ring (circle) with a given radius."""
    turtle.penup()
    turtle.goto(0, -radius)  # Move to the starting position
    turtle.pendown()
    turtle.circle(radius)  # Draw the circle

def draw_heart_with_rings(num_rings):
    """Draw a heart shape made of rings."""
    turtle.speed(0)  # Fastest drawing speed
    turtle.color("red")  # Set the color for the rings

    # Draw the rings
    for i in range(num_rings):
        draw_ring(50 + i * 10)  # Increase the radius for each ring

    # Draw the heart shape
    turtle.penup()
    turtle.goto(0, -50)  # Move to the starting position for the heart
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("pink")  # Fill color for the heart
    turtle.left(140)
    turtle.forward(224)  # Move forward to create the left side of the heart
    turtle.circle(-112, 200)  # Create the left curve of the heart
    turtle.left(120)
    turtle.circle(-112, 200)  # Create the right curve of the heart
    turtle.forward(224)  # Move forward to complete the heart shape
    turtle.end_fill()

def main():
    turtle.bgcolor("white")  # Set the background color
    draw_heart_with_rings(7)  # Draw 7 rings
    turtle.hideturtle()  # Hide the turtle after drawing
    turtle.done()  # Finish the drawing

if __name__ == "__main__":
    main()