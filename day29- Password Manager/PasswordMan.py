from tkinter import *
from tkinter import messagebox
from random import shuffle, choice
import pyperclip
import json
import cryptography
from cryptography.fernet import Fernet


# json.load(#data file)
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
        password_entry.delete(0, 'end')
        password_entry.insert(0, f"{password}")
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def generate_and_store_key(filename="secret.key"):
    """Generate a new key and store it in a file."""
    key = Fernet.generate_key()
    with open(filename, "wb") as key_file:
        key_file.write(key)

generate_and_store_key()
def load_key(key_filename="secret.key"):
    """Loads a previously generated key (bytes) from a file."""
    with open(key_filename, "rb") as key_file:
        key = key_file.read()
    return key

# Load the key once, then create the Fernet object
key = load_key("secret.key")
fernet = Fernet(key)

def on_add():
    new_data = {
        website_entry.get(): {
            "email": email_user_entry.get(),
            "password": password_entry.get()
        }
    }
    if len(password_entry.get()) == 0 or len(email_user_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showerror("please enter information", "Please enter required information.")
    else:
        is_okay = messagebox.askokcancel(title=website_entry.get(), message=f"these are the credentials entered: \n"
                                                                            f"Email: {email_user_entry.get()}\n"
                                                                            f"Password: {password_entry.get()}\n"
                                                                            f"Is this okay to save?")
        if is_okay:
            try:
                with open("my_passwords.json", "rb") as encrypted_file:
                    encrypted_content = encrypted_file.read()  # Read all bytes
                decrypted_content = fernet.decrypt(encrypted_content)  # Decrypt to get JSON bytes
                data = json.loads(decrypted_content.decode("utf-8"))  # Parse JSON into Python dict

            except FileNotFoundError:
                # --- If file doesn't exist, create a new encrypted file with new_data ---
                data = new_data

            except Exception as e:
                # If decryption fails or any other error, you might handle it here
                messagebox.showerror("Error", f"Could not read or decrypt data:\n{e}")
                return
            else:
                # --- Update the existing data with new_data ---
                data.update(new_data)

                # 5. Encrypt and save the updated data
            try:
                json_string = json.dumps(data, indent=4)  # Convert Python dict to JSON string
                encrypted_data = fernet.encrypt(json_string.encode("utf-8"))  # Encrypt the JSON

                with open("my_passwords.json", "wb") as encrypted_file:
                    encrypted_file.write(encrypted_data)

            except Exception as e:
                messagebox.showerror("Error", f"Could not write or encrypt data:\n{e}")
                return

            # KEEPING THIS ORIGINAL CODE FOR REFERENCE
            #     with open("my_passwords.json", "r") as add_password:
            #         # raeding old data
            #         data = json.load(add_password)
            #
            # except FileNotFoundError:
            #     with open("my_passwords.json", "w") as add_password:
            #         json.dump(new_data, add_password, indent=4)
            # else:
            #     # updating old data with new data
            #     data.update(new_data)
            #     with open("my_passwords.json", "w") as add_password:
            #         # adding new data to file with proper formatting
            #         json.dump(data, add_password, indent=4)
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


def search_pass():
    try:
        with open("my_passwords.json", "r") as add_password:
            # raeding old data
            data = json.load(add_password)
            searched_website = website_entry.get()
    except FileNotFoundError:
        messagebox.showerror(title="File Error", message="You have no passwords on file")
    else:
        for web, value in data.items():
            if web == searched_website:
                messagebox.askokcancel(title=f"Information For: {searched_website.capitalize()}",
                                       message=f"Email: {data[searched_website]['email']} \n"
                                               f"Password: {data[searched_website]['password']}")
                pyperclip.copy(data[searched_website]['password'])


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
website_entry = Entry(width=33)
email_user_entry = Entry(width=52)
password_entry = Entry(width=33)

# buttons
add_pass_button = Button(text="Add", width=44, command=on_add)
generate_pass_button = Button(text="Generate Password", command=gen_password)
search_pass_button = Button(text="Search", width=15, command=search_pass)

# postioning
canvas.grid(column=1, row=0)

website_label.grid(column=0, row=1)
email_user_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "example@gmail.com")
password_entry.grid(column=1, row=3)

add_pass_button.grid(column=1, row=4, columnspan=2)
search_pass_button.grid(column=2, row=1)
generate_pass_button.grid(column=2, row=3)

window.mainloop()
