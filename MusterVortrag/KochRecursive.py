# Your basic Koch triangle
# inspired from (c) https://trinket.io/python/8c8b7f567e

import turtle
import math

def koch_segment(t, lenght, currentdepth):
    '''draws a Segment with the current depth

    Parameters
    ----------
    t : turtle object
        The turtle window object to be drawed to
    lenght : float
        The length of the line Koch is drawed to
    currentdepth : integer
        The current iteration depth of Koch - 1 is straight line of length run

    Returns
    -------
    None
    '''
    if currentdepth == depth:
        # Just draw a segment
        t.fd(lenght)
    else:
        currentlength = lenght / 3.0
        # Make each straight bit into a smaller version of ourselves
        koch_segment(t, currentlength, currentdepth + 1)
        t.left(60)
        koch_segment(t, currentlength, currentdepth + 1)
        t.right(120)
        koch_segment(t, currentlength, currentdepth + 1)
        t.left(60)
        koch_segment(t, currentlength, currentdepth + 1)


def setup_turtle(depth):
    ''' set up turtle and define lenght according screen size'''
    wn = turtle.Screen()
    wx = wn.window_width() * .5
    wh = wn.window_height() * .5
    base_length = 2.0 / math.sqrt(3.0) * wh

    myTurtle = turtle.Turtle()
    myTurtle.speed(300 * (depth + 1))
    myTurtle.penup()
    myTurtle.setposition((-wx / 2, -wh / 2))
    myTurtle.pendown()
    myTurtle.left(60)

    return myTurtle, base_length


# main program
# depth is the global recursion steps to be reached, startdepth where to start
depth = 6
startdepth = 1

myTurtle, base_length = setup_turtle(depth)
# initialize turtle

for ii in range(3):
    # with parameter 3 draw three lines of the triangle base shape
    koch_segment(myTurtle, base_length, startdepth)
    myTurtle.right(120)

turtle.exitonclick()
# close drawing window on click
