------------------------------------------------------------------------------------
Clear Screen Methods

If you run the program in a DOS/Linux terminal you could use this (or the following one too):

    import os
     
    def clear():  # Cross-platform clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

The above will not work in the PyCharm output (Run) console. Use this instead:

    def clear():  # Prints 50 blank lines
        print("\n" * 50)

------------------------------------------------------------------------------------

Docsctrings - Give custom functions descriptions.
Example

""" Put the Info in here just below the definition """

-----------------------------------------------------------------------------------

Basic Turtle Screen

from turtle import Turtle, Screen

screen = Screen(height = 600, width = 600)


screen.exitonclick()

----------------------------------------------------------------------------------
basic tkinter window

import tkinter

window = tkinter.Tk()


window.mainloop()

------------------------------------------------------------------------------------

## Notes, Move this later
print(iss_loc) - Status reponse
print(iss_loc.status_code) - Just status Code