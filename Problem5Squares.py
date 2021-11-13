# Producing squares with turtle

import turtle

def drawSqaure(t, sz):
    """"Get turtle t to draw a square of sz side"""""

    for i in range(4):
        t.forward(sz)
        t.left(90)



wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
drawSqaure(alex, 30)
drawSqaure(alex, 50)
drawSqaure(alex, 70)
drawSqaure(alex, 90)


wn.exitonclick()