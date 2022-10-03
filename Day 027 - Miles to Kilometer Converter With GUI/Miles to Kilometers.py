import tkinter

def conv_to_km():
    conversion = float(entry_mi.get())*1.6
    entry_km.delete(0,tkinter.END)
    entry_km.insert(tkinter.END, string=f"{conversion}")

def conv_to_miles():
    conversion = float(entry_km.get())/1.6
    entry_mi.delete(0,tkinter.END)
    entry_mi.insert(tkinter.END, string=f"{conversion}")

window = tkinter.Tk()
window.title("My Python Program")
window.minsize(width=300, height=150)
window.maxsize(width=300, height=150)

header = tkinter.Label(text="Miles to Kilometers", font=("Courior", 15, "bold"))
header.place(x=0, y=0)

button_mi = tkinter.Button(text = "To Km", command=conv_to_km, justify='center')
button_mi.place(x=200, y=45)

entry_mi = tkinter.Entry(width= 10, justify='center')
entry_mi.place(x=125, y=50)

banner_mi = tkinter.Label(text="     Miles = ", font=("Courior", 10, "bold"))
banner_mi.place(x=25, y=50)

button_km = tkinter.Button(text = "To Miles", command=conv_to_miles, justify='center')
button_km.place(x=200, y=95)

entry_km = tkinter.Entry(width= 10, justify='center')
entry_km.place(x=125, y=100)

banner_km = tkinter.Label(text="Kilometers = ", font=("Courior", 10, "bold"))
banner_km.place(x=25, y=100)



window.mainloop()