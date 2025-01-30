import turtle

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(0)
    
    for x in range(width):
        for y in range(height):
            real = xmin + (x / width) * (xmax - xmin)
            imag = ymin + (y / height) * (ymax - ymin)
            c = complex(real, imag)
            m = mandelbrot(c, max_iter)
            color = (m / max_iter, m / max_iter, m / max_iter)  # Grayscale
            turtle.pencolor(color)
            turtle.goto(x - width // 2, y - height // 2)
            turtle.dot(1)

    turtle.update()

# Set up the screen
turtle.setup(800, 600)
draw_mandelbrot(-2.0, 1.0, -1.5, 1.5, 800, 600, 100)
turtle.done()