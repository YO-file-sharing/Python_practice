import turtle

a = turtle.Pen()
b = turtle.Pen()

a.color("#FF0000", "#FFFF00")
b.color("#0000FF", "#8A2BE2")

def Tag(c):
    c.forward(100)

Tag(a)
b.left(180)
Tag(b)
a.begin_fill()
a.circle(100)
a.end_fill()
b.begin_fill()
b.circle(100)
b.end_fill()


turtle.done()