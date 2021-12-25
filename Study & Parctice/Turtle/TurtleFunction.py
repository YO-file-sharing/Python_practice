from turtle import *

def T_Func1(a1, angle):
    for a in range(a1):
        forward(a1)
        left(angle)

def T_Func2(a2):
    for a in range(a2):
        forward(a2)
        if a2 % 2 == 1:
            left(90)
        else:
            right(90)

