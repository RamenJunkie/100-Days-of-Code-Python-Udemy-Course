import tkinter

window = tkinter.Tk()
window.title("My Python Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="A Basic Label", font=("Courior", 20, "bold"))
my_label.pack()
## side = "left, bottom, etc
## expand = True  = centers things

## Two ways to change the label
my_label["text"] = "New Label Text"
my_label.config(text = "A Different Label for Text")

def clicker():
    #my_label["text"] = "Ohh yeah baby...."
    my_label["text"] = entry.get()


button = tkinter.Button(text = "Click me!", command= clicker)
button.pack()


entry = tkinter.Entry()
entry.pack()
result = entry.get()

window.mainloop()

## OTHER NOTES
## pack() Just layers them on
## place( x= , y= ) Places at coordinates
## grid(column = , row = ) = Columns, relative to everything placed IE put something in each column and row\
## window.config(padx = XX, pady = XX)    - Add Padding
