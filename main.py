from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- FIND PASSWORD  ------------------------------- #
def find_pass():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=f"{website_entry.get()}", message=f"email:{data[website_entry.get()]['email']}\n"
                                                                        f"password:{data[website_entry.get()]['password']}")

    except KeyError:
        messagebox.showerror(title="Error", message=f"No Details for the {website_entry.get()} exist")

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]

    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    password="".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    new_data={
        website_entry.get():{
            "email":email_entry.get(),
            "password":password_entry.get(),
        }
    }

    if len(website_entry.get())==0 or len(email_entry.get())==0 or len(password_entry.get())==0:
        messagebox.showwarning(title="AppBrewery", message="Please don't have any fields empty.")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
    else:
        try:
            with open("data.json", "r") as data_file:  #json dosyası okuma modunda açıldı.
                data=json.load(data_file)    #json formatında .load okuma metodu dosya konusundaki read gibi
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=1)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            data.update(new_data)  #eski veriler yeni verilerle güncellendi
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=1)  #daha sonra burada da yeni veriler json dosyasına yazıldı.

        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

img=PhotoImage(file="logo.png")
canvas=Canvas(height=200, width=200)
canvas.create_image((100,100), image=img)
canvas.grid(row=0, column=1)

website_label=Label(text="Website: ")
website_label.grid(row=1, column=0)

website_entry=Entry(width=30)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")

search_button=Button(width=14, text="Search", command=find_pass)
search_button.grid(row=1, column=2, sticky="w")


email_username_label=Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

email_entry=Entry(width=51)
email_entry.insert(0,"uguryasinkucuk@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_label=Label(text="Password: ")
password_label.grid(row=3, column=0)

password_entry=Entry(width=25)
password_entry.grid(row=3, column=1, sticky="w")

generate_pass_button=Button(width=14, text="Generate Password", command=password_generate)
generate_pass_button.grid(row=3, column=2, sticky="w")

add_button=Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()