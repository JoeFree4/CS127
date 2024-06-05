#Joseph Freeman
#joseph.freeman41@myhunter.cuny.edu
#March 1, 2024

#this program asks the user for the hexcode of a color and then displays a turtle that color


import turtle

hex_string = input("Enter a hex string: ")

wn = turtle.Screen()
joe = turtle.Turtle()
joe.shape("turtle")
joe.color(hex_string)

wn.exitonclick
