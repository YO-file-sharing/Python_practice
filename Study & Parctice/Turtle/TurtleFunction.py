from turtle import *

def T_Func1(a1, angle):
    pen1 = Pen()
    for a in range(a1):
        pen1.forward(a)
        pen1.left(angle)

def T_Func2(a2):
    pen2 = Pen()
    for a in range(a2):
        pen2.forward(a)
        if a2 % 2 == 1:
            pen2.left(90)
        else:
            pen2.right(90)

