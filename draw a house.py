import turtle

def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def draw_triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

turtle.speed(1)

# Draw the house
draw_square()

# Draw the roof
turtle.left(90)
turtle.forward(100)
turtle.right(30)
draw_triangle()

turtle.done()