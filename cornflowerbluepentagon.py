#Joseph Freeman
#joseph.freeman41@myhunter.cuny.edu
#February 28, 2024

#this program creates a cornflower blue pentagon, with turtle shape stamps

import turtle
wn = turtle.Screen()
joe = turtle.Turtle()
joe.shape("turtle")
joe.color("cornflowerblue")


for i in range(5):
    joe.forward(100)
    joe.stamp()
    joe.left(360/5)

wn.exitonclick()
