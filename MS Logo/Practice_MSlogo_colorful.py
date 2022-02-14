# 色付き MS ロゴ

import turtle as t
t.hideturtle()
t.speed(150)
t.width(10)

def main(color1,x,y):
    t.color(color1)
    t.penup()
    t.goto(x,y)
    t.pendown()

    for a in range(10):
        t.forward(100)
        if a % 2 == 0:
            t.right(90)
            t.forward(10)
            t.right(90)
        else:
            t.left(90)
            t.forward(10)
            t.left(90)

    t.forward(100)

    for b in range(4):
        t.left(90)
        t.forward(100)

# 左上 オレンジ
main(color1="#F25022", x=-110, y=110)

# 右上 グリーン
main(color1="#7FBA00", x=10, y=110)

# 左下 ブルー
main(color1="#00A4EF", x=-110, y=-10)

# 左下 イエロー
main(color1="#FFB900", x=10, y=-10)

t.done()