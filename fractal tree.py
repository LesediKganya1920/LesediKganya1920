import turtle

def draw_branch(branch_length):
    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 15)
        turtle.left(40)
        draw_branch(branch_length - 15)
        turtle.right(20)
        turtle.backward(branch_length)

# Set up the turtle
turtle.speed(0)
turtle.left(90)
turtle.color("brown")
turtle.penup()
turtle.backward(100)
turtle.pendown()
turtle.pensize(2)

# Draw the tree
draw_branch(100)

turtle.done()