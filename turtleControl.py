#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Mar 20,2024

import turtle

joe = turtle.Turtle()
myWin = turtle.Screen()     #The graphics window
commands = input("Please enter a command string: ")

for ch in commands:
    #perform action indicated by the character
    if ch == 'F':            #move forward
        joe.forward(50)
    elif ch == 'L':          #turn left
        joe.left(90)
    elif ch == 'R':          #turn right
        joe.right(90)
    elif ch == '^':          #lift pen
        joe.penup()
    elif ch == 'v':          #lower pen
        joe.pendown()
    elif ch == 'B':         #moves turtle backwards 50 steps
        joe.backward(50)
    elif ch == 'S':         #makes the turtle stamp
        joe.stamp()
    elif ch == 'l':         #turns turtle 45 degrees to the left
        joe.left(45)
    elif ch == 'r':         #turns turtle 45 degrees to the right
        joe.right(45)
    elif ch == 'p':         #change the pen color to purple
        joe.color("purple")

    else:                   #for any other character, print an error message 
        print("Error: do not know the command:", ch) #typo, was c before

print("See graphics window for your image")
myWin.exitonclick()         #Close the window when clicked




