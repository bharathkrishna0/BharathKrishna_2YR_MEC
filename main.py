import turtle
import math

# Color definitions
maroon = "#61111c"
orange = "#de8116"
yellow = "#e4cf27"
white = "white"
green = "#38642a"
purple = "#885196"

turtle.speed(0)
turtle.hideturtle()


def draw_zigzag_ring(radius, count, amplitude, color):
    points = []
    for i in range(count * 2):
        angle = i * (360 / (count * 2))
        r = radius + amplitude if i % 2 == 0 else radius - amplitude
        x = r * math.sin(math.radians(angle))
        y = r * math.cos(math.radians(angle))
        points.append((x, y))
    turtle.penup()
    turtle.goto(points[0][0], -points[0][1])
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x, y in points:
        turtle.goto(x, -y)
    turtle.goto(points[0][0], -points[0][1])
    turtle.end_fill()

def draw_circle(radius, color):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_sector(center_x, center_y, radius, start_angle, extent_angle, color):
    turtle.penup()
    turtle.goto(center_x, center_y)
    turtle.setheading(start_angle)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(center_x, center_y)
    for step in range(extent_angle + 1):
        angle = start_angle + step
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        turtle.goto(x, y)
    turtle.goto(center_x, center_y)
    turtle.end_fill()

def draw_hexagon(size, color):
    turtle.penup()
    turtle.goto(0,0)
    r = size / (2 * math.sin(math.pi / 6))
    points = []
    for i in range(6):
        angle = math.radians(60 * i + 30)
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        points.append((x, y))
    turtle.goto(points[0])
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x, y in points:
        turtle.goto(x, y)
    turtle.goto(points[0])
    turtle.end_fill()

def draw_octagon(size, color):
    turtle.penup()
    turtle.goto(0,0)
    r = size / (2 * math.sin(math.pi / 8))
    points = []
    for i in range(8):
        angle = math.radians(45 * i + 22.5)
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        points.append((x, y))
    turtle.goto(points[0])
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x, y in points:
        turtle.goto(x, y)
    turtle.goto(points[0])
    turtle.end_fill()

def draw_pinwheel(radius, wedges, color1, color2):
    angle = 360 / wedges
    for i in range(wedges):
        turtle.penup()
        turtle.goto(0,0)
        turtle.setheading(i * angle)
        turtle.pendown()
        turtle.fillcolor(color1 if i % 2 == 0 else color2)
        turtle.begin_fill()
        turtle.forward(radius)
        turtle.left(120)
        turtle.forward(radius/3)
        turtle.left(120)
        turtle.forward(radius)
        turtle.goto(0,0)
        turtle.end_fill()

# Draw outer zigzag rings
draw_zigzag_ring(180, 18, 18, maroon)
draw_zigzag_ring(160, 18, 14, orange)
draw_zigzag_ring(140, 18, 10, yellow)
draw_zigzag_ring(120, 18, 7, white)

# Draw main green circle
draw_circle(100, green)

# Draw maroon hexagon (central - fits inside green)
draw_hexagon(56, maroon)

# Draw green octagon (fits inside hexagon)
draw_octagon(46, green)

# Draw central pinwheel
draw_pinwheel(32, 8, white, maroon)



turtle.done()
