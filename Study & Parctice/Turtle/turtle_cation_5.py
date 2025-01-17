from random import randint
import turtle as t

t.tracer(False)
t.hideturtle()
# t.speed(10000)
t.penup()

def main(x1, x2, y1, y2, Color):
    t.goto(x1,y1)
    t.color(Color)
    for i in range(5000):
        t.goto(randint(x1, x2), randint(y1, y2))
        t.pendown()
        t.circle(randint(1, 5))
        t.penup()

main(x1=-205, x2=-5, y1=5, y2=205, Color = "#F25022")
main(x1=5, x2=205, y1=5, y2=205, Color = "#7FBA00")
main(x1=-205, x2=-5, y1=-205, y2=-5, Color = "#00A4EF")
main(x1=5, x2=205, y1=-205, y2=-5, Color = "#FFB900")

t.done()