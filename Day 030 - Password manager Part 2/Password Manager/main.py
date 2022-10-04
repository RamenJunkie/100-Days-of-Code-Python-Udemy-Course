from tkinter import *
from tkinter import messagebox
BACKGROUND = "logo.png"
SAVEFILE = "data.json"
from defaults import *
from Password_Generator import *
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def search_site():
    site = site_entry.get()

    try:
        with open(SAVEFILE, mode="r") as infile:
            data = json.load(infile)

        try:
            data[site]
        except:
            messagebox.showerror(title="No Entry", message=f"Sorry, No entry for {site}")
        else:
            messagebox.showerror(title=site, message=f"Username: {data[site]['email']}\n"
                                                     f"Password: {data[site]['password']}")
            window.clipboard_clear()
            window.clipboard_append(data[site]["password"])
    except FileNotFoundError:
        messagebox.showerror(title="No Entry", message=f"Sorry, No entry for {site}")


# -------------------------- GENERATE PASSWORD ------------------------------- #
def new_pass():
    generator = pass_gen()
    password = generator.make_password()
    pass_entry.delete(0,END)
    pass_entry.insert(END, string=password)
    window.clipboard_clear()
    window.clipboard_append(password)

# ----------------------------- RESET THE FORM ------------------------------- #
def clear_form():
    pass_entry.delete(0, END)
    mail_entry.delete(0, END)
    mail_entry.insert(END, string=email)
    site_entry.delete(0, END)
    site_entry.focus()

# ---------------------------- SAVE PASSWORD ------------------------------- #
def submit_form():
    if not site_entry.get() or not mail_entry.get() or not pass_entry.get():
        messagebox.showerror(title = "Error!", message="Do not leave any fields blank.")
    else:
        sure = messagebox.askokcancel(title="Confirm", message = f"Are you sure you want to save\nWebsite: {site_entry.get()}\nUsername: {mail_entry.get()}\nPassword: {pass_entry.get()}")
        if sure:
            new_entry = {
                site_entry.get(): {
                    "email": mail_entry.get(),
                    "password": pass_entry.get(),
                }
            }
            try:
                with open(SAVEFILE, mode="r") as infile:
                    data = json.load(infile)
                    data.update(new_entry)
            except FileNotFoundError:
                data = new_entry



            with open(SAVEFILE, mode="w") as output:
                json.dump(data, output, indent=4)

            messagebox.showinfo(title = "Success!", message = f"Saved {site_entry.get()}, to the database.")
            clear_form()


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

site_entry = Entry(width=20)
site_entry.grid(column=2, row=2)
site_result = site_entry.get()

search_button = Button(text = "Search", command=search_site, width=15)
search_button.grid(column=3, row=2)

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

clear_button = Button(text = "Reset Form", command=clear_form, width=15)
clear_button.grid(column=1, row=5)

submit_button = Button(text = "Add", command=submit_form, width=38)
submit_button.grid(column=2, row=5, columnspan=2)



window.mainloop()