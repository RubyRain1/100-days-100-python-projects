from tkinter import *
from tkinter import messagebox
from random import shuffle, choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [f"{choice(numbers)}{choice(letters)}{choice(symbols)}" for _ in symbols]
    shuffle(password_list)

    password = "".join(password_list)
    print(password)
    if len(password_entry.get()) == 0:
        password_entry.insert(0, f"{password}")
        pyperclip.copy(password)
    else:
        password_entry.delete(0,'end')
        password_entry.insert(0, f"{password}")
        pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def on_add():
    if len(password_entry.get()) == 0 or len(email_user_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showerror("please enter information", "Please enter required information.")
    else:
        is_okay = messagebox.askokcancel(title=website_entry.get(), message=f"these are the credentials entered: \n"
                                                                            f"Email: {email_user_entry.get()}\n"
                                                                            f"Password: {password_entry.get()}\n"
                                                                            f"Is this okay to save?")
        if is_okay:
            with open("my_passwords.txt", "a") as add_password:
                add_password.write(f"{website_entry.get()} | {email_user_entry.get()} |"
                                   f" {password_entry.get()}\n")
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)

# labels
website_label = Label(text="Website:")
email_user_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# entries
website_entry = Entry(width=52)
email_user_entry = Entry(width=52)
password_entry = Entry(width=33)

# buttons
add_pass_button = Button(text="Add", width=44, command=on_add)
generate_pass_button = Button(text="Generate Password", command=gen_password)

# postioning
canvas.grid(column=1, row=0)

website_label.grid(column=0, row=1)
email_user_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "example@gmail.com")
password_entry.grid(column=1, row=3)

add_pass_button.grid(column=1, row=4, columnspan=2)
generate_pass_button.grid(column=2, row=3)
window.mainloop()
