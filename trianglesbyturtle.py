#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Apr 1, 2024




import turtle

wn = turtle.Screen()

joe = turtle.Turtle()

def triangle(joe, length):
    if length > 10:
        for _ in range(3):
            joe.forward(length)
            joe.left(120)
        triangle(joe, length/2)

def nestedTriangle(joe, length):
    if length > 10:
        for _ in range(3):
            joe.forward(length)
            joe.left(120)
            nestedTriangle(joe, length/2)


triangle(joe, 100)


wn.exitonclick()

