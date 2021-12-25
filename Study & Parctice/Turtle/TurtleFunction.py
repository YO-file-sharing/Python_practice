from turtle import *

def T_Func1(a1, angle):
    for a in range(a1):
        forward(a)
        left(angle)

def T_Func2(a2):
    for a in range(a2):
        forward(a2)
        right(90)
        forward(1)
        if a % 2 == 1:
            left(90)
        else:
            right(90)

