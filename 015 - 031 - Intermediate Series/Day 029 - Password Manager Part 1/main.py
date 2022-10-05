from tkinter import *
from tkinter import messagebox
BACKGROUND = "logo.png"
SAVEFILE="data.md"
from defaults import *
from Password_Generator import *

def make_popup(message):
    popup = Tk()
    popup.geometry("200x100")
    popup.config(padx=20, pady=20)
    poplabel = Label(popup, text=message, font=("Courior", 10, "normal"))
    poplabel.pack()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def new_pass():
    generator = pass_gen()
    password = generator.make_password()
    pass_entry.delete(0,END)
    pass_entry.insert(END, string=password)
    window.clipboard_clear()
    window.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def submit_form():
    if not site_entry.get() or not mail_entry.get() or not pass_entry.get():
        messagebox.showerror(title = "Error!", message="Do not leave any fields blank.")
#    elif "@" not in mail_entry.get() or "." not in mail_entry.get():
#        messagebox.showerror(title="Error!", message = "Invalid eMail Address!")
    else:
        sure = messagebox.askokcancel(title="Confirm", message = f"Are you sure you want to save\nWebsite: {site_entry.get()}\nUsername: {mail_entry.get()}\nPassword: {pass_entry.get()}")
        if sure:
            with open(SAVEFILE, mode="a") as output:
                output.write(f"{site_entry.get()}|{mail_entry.get()}|{pass_entry.get()}\n")
            messagebox.showinfo(title = "Success!", message = f"Saved {site_entry.get()}, to the database.")
            pass_entry.delete(0, END)
            mail_entry.delete(0, END)
            mail_entry.insert(END, string=email)
            site_entry.delete(0, END)
            site_entry.focus()

    # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Pass Password Keeper")
window.config(padx= 10, pady= 30)
bgimg = PhotoImage(file = BACKGROUND)
window.minsize(400, 350)

canvas = Canvas(height=220, width=350)
canvas.create_image(125 , 110, image = bgimg)
canvas.grid(column=2, row=1, columnspan=3 )

site_label = Label(text="Website: ", font=("Courior", 10, "bold"), justify="right", width=15)
site_label.grid(column=1, row = 2)
username_label = Label(text="Username or eMail: ", font=("Courior", 10, "bold"), justify="right", width=15)
username_label.grid(column=1, row=3)
pass_label = Label(text="Password: ", font=("Courior", 10, "bold"), justify="right", width=15)
pass_label.grid(column=1, row=4)

site_entry = Entry(width=45)
site_entry.grid(column=2, row=2, columnspan=2)
site_result = site_entry.get()
site_entry.focus()
mail_entry = Entry(width=45)
mail_entry.insert(END, string=email)
mail_entry.grid(column=2, row=3, columnspan=2)
mail_result = mail_entry.get()

pass_entry = Entry(width=20)
pass_entry.grid(column=2, row=4)
pass_result = pass_entry.get()

gen_button = Button(text = "Generate Password", command=new_pass, width=15)
gen_button.grid(column=3, row=4)

submit_button = Button(text = "Add", command=submit_form, width=38)
submit_button.grid(column=2, row=5, columnspan=2)



window.mainloop()