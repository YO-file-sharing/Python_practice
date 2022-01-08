import tkinter
from tkinter.constants import X

root = tkinter.Tk()
root.resizable(width=False, height=False)

IS_CALA = False

MaxShowLen = 18
CurrentShow = tkinter.StringVar()
CurrentShow.set("0")

def Demo():
    root.minsize(320,480)
    root.title("calculator")
    label = tkinter.Label(root, textvariable=CurrentShow, bg="black", anchor="e", bd=5, fg="white", font=("", 20))
    label.place(x=20, y=50, width=280, height=50)

if __name__ == "__main__":
    Demo()