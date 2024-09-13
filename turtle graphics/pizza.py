import turtle as t

tim = t.Turtle()
screen = t.Screen()
BACKGROUND = "#9EC388"
CRUST = "#ECA84F"
SAUCE = "#AD0509"
CHEESE = "#FBC70F"
PEPPERONI = [
    [-70, 5],
    [-85, 75],
    [-25, -50],
    [-15, 0],
    [-25, 50],
    [-30, 105],
    [15, -50],
    [20, 20],
    [20, 100],
    [60, 56],
    [71, 115],
    [80, -10],
    [0, 130],
]
screen.bgcolor(BACKGROUND)
screen.title("Pizza Shop")
tim.speed("fastest")
tim.pensize(5)
tim.shape("circle")


def draw_circle(radius, line_color, fill_color):
    """draw a circle for the pizza"""
    tim.color(line_color)
    tim.fillcolor(fill_color)
    tim.begin_fill()
    tim.circle(radius)
    tim.end_fill()


def move_turtle(x, y):
    """move turtle to the destination based on the coordinates"""
    tim.up()
    tim.goto(x, y)
    tim.down()


# start to draw the pizza
move_turtle(0, -100)
draw_circle(150, CRUST, CRUST)
move_turtle(0, -75)
draw_circle(125, SAUCE, CHEESE)

for location in PEPPERONI:
    tim.pu()
    move_turtle(location[0], location[1])
    tim.dot(20, SAUCE)

# cut the pizza
move_turtle(0, 50)
tim.color(BACKGROUND)
for x in range(0, 8):
    tim.pd()
    tim.left(45)
    tim.forward(150)
    tim.pu()
    tim.backward(150)
screen.exitonclick()
