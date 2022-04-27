from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import pandas

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    # password_list.append(str(random_letters))
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list += [choice(symbols) for char in range(randint(2, 4))]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list += [choice(numbers) for char in range(randint(2, 4))]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }
    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Error", message="Please, do not leave any field empty ")
    else:
        # is_user_agree = messagebox.askyesnocancel(title=website_name, message=f"These are details of your password: "
        # f"\nEmail: {email_username} \nPassword: {password} \nDo you agree to save this data in data_file?")
        # if is_user_agree:
        #         with open("data.json", mode="w") as data_file:
        #           json.dump(new_data, data_file)
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            new_data.update(data)
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file,  indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

def search_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Eror", message=f"There is no file named{website}")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            raise messagebox.showinfo(title="Error", message=f"There is no website named {website}")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid( row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_label.focus()
email_username_label = Label(text="Emaail/Username:",height=1)
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_input = Entry(width=46)
website_input.grid(row=1, column=1)
website_input.focus()
email_username_input = Entry(width=65)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0, "YOUR EMAIL")
password_input = Entry(width=46)
password_input.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password", highlightthickness=0, bg="white", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=56, bg="white", command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", bg="white",width=14, highlightthickness=0, command=search_password)
search_button.grid(row=1, column=2, columnspan=5)

window.mainloop()