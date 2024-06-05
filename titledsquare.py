#joseph Freeman
#joseph.freeman41@myhunter.cuny.edu
#February 26, 2024

import turtle
wn = turtle.Screen()

# Create Turtle
joe = turtle.Turtle()

for i in range(5, 301, 5):          # Loop turtle to walk forward and turn left
    joe.forward(i)
    joe.left(91)

wn.exitonclick
