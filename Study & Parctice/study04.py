import random as r
from turtle import xcor

def GuessNum(X):
    global Q1, Q2
    Q1 = Q2 = 0
    for a in range(X) :
        Num = r.randint(0,1)
        if Num == 0:
            Q1 += 1
        else:
            Q2 += 1
    return Q1, Q2


GuessNum(5000)
print(Q1)
print(Q2)
