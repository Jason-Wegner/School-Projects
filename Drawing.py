import turtle
def draw_square():
    t = turtle.Turtle()
    t.fd(side_length)
    t.rt(90)
    t.fd(side_length)
    t.rt(90)
    t.fd(side_length)
    t.rt(90)
    t.fd(side_length)
    t.hideturtle()
    turtle.done()

def draw_triangle():
    t = turtle.Turtle()
    t.rt(60)
    t.fd(side_length)
    t.rt(120)
    t.fd(side_length)
    t.rt(120)
    t.fd(side_length)
    t.hideturtle()
    turtle.done()

def draw_rectangle():
    t = turtle.Turtle()
    t.fd(side_lengtha)
    t.rt(90)
    t.fd(side_lengthb)
    t.rt(90)
    t.fd(side_lengtha)
    t.rt(90)
    t.fd(side_lengthb)
    t.hideturtle()
    turtle.done()

shape = input("Would you like me to draw a square, triangle or rectangle? ")
if shape == "square":
    side_length = int(input("What size would you like your square? (100-500) "))
    draw_square()

if shape == "triangle":
    side_length = int(input("What size would you like your triangle? (100-500) "))
    draw_triangle()

if shape == "rectangle":
    side_lengtha = int(input("What length would you like your rectangle? (100-500) "))
    side_lengthb = int(input("What width would you like your rectangle? (100-500) "))
    draw_rectangle()