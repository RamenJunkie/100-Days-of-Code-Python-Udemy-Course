from turtle import *
import turtle as tur
def getPosition(i,j):
    print("clicked")
    print(f"({i},{j})")
    return

def mainscr():
    tur.onscreenclick(getPosition)
    tur.mainloop()
mainscr()