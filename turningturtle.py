#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#March 1, 2024

#This program allows the turtle to move forward 100units for ever turn made

import turtle

wn = turtle.Screen()
joe = turtle.Turtle()

for i in range(5):
    degrees = int(input("Enter a number: "))
    joe.left(degrees)
    joe.forward(100)

wn.exitonclick()
