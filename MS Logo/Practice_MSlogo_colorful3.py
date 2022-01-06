import random as r
import turtle as t

t.tracer(False)
t.hideturtle()
# t.speed(10000)
t.penup()

def main(x1, x2, y1, y2, Color):
    t.goto(x1,y1)
    t.pendown()
    t.color(Color)
    for i in range(10000):
        t.goto(r.randint(x1, x2), r.randint(y1, y2))
    t.penup()

main(x1=-205, x2=-5, y1=5, y2=205, Color = "#F25022")
main(x1=5, x2=205, y1=5, y2=205, Color = "#7FBA00")
main(x1=-205, x2=-5, y1=-205, y2=-5, Color = "#00A4EF")
main(x1=5, x2=205, y1=-205, y2=-5, Color = "#FFB900")

t.done()