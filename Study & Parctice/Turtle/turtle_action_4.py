import turtle as t
import TurtleFunction

t.color("#FF0000")
t.tracer(False)
for a in range(300):
    t.forward(a)
    t.left(a)


i = 500
TurtleFunction.T_Func1(i, 95)

t.done()