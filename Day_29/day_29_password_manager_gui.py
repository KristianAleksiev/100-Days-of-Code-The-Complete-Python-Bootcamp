### Day 29 - Building a password manager GUI app with Tkinter

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

### PASSWORD GENERATING FUNCTIONALITY


def password_generation():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
               'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pw_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    pw_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = pw_symbols + pw_numbers + pw_letters
    random.shuffle(password_list)

    password = "".join(password_list) #=> Joining the elements
    password_entry.insert(0, password)
    pyperclip.copy(password) #=> Password ready for Paste after generating

### SAVE PASSWORD FUNCTIONALITY


def add():
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty field!", message="Please fill the empty fields")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the entered details: \n"
                                                          f"Email:{email}\n Password: {password} \n"
                                                          f"Do you wish to save?")
        if is_ok:
            with open("generated_passwords.txt", mode="a") as passwords_file:
                passwords_file.write(f"Website: {web}  ||  Username: {email}  ||  Password: {password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)
                web_entry.focus()


### USER INTERFACE SETUP

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)  # => Middle of the screen
canvas.grid(row=0, column=1)

### Creating the labels

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(text="Email / Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

### Creating the entries

web_entry = Entry(width=46)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()  # => Cursor at this entry when program is strated

email_entry = Entry(width=46)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "test@gmail.com")  # => Prepopulating the entry, 0 for positioning, END for at end

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

### Creating the buttons

generate_button = Button(text="Generate password", command=password_generation)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=48, command=add)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
