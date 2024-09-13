import turtle

# Set up the turtle screen
turtle.setup(width=600, height=600)
wn = turtle.Screen()
wn.bgcolor("white")

# Create a turtle to draw the heart
pen = turtle.Turtle()
pen.color("red")
pen.speed(0)  # Max speed


def draw_heart(scale):
    pen.begin_fill()
    pen.left(50)
    pen.forward(133 * scale)
    pen.circle(50 * scale, 200)
    pen.right(140)
    pen.circle(50 * scale, 200)
    pen.forward(133 * scale)
    pen.end_fill()


def draw_3d_heart(layers, scale_factor):
    for i in range(layers):
        pen.penup()
        pen.goto(-30, -200 + i * 4)
        pen.pendown()
        scale = 1 - (i * scale_factor)
        pen.fillcolor((1.0, 0.2 + 0.8 * (1 - scale), 0.2 + 0.8 * (1 - scale)))
        draw_heart(scale)
        pen.setheading(0)


# Draw multiple layers to simulate a 3D effect
draw_3d_heart(30, 0.02)

# Hide the turtle and display the result
pen.hideturtle()

# Keep the window open until closed by the user
turtle.done()
