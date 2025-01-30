import turtle

def draw_star(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

turtle.bgcolor("black")
turtle.color("yellow")
turtle.speed(2)

draw_star(100)

turtle.done()