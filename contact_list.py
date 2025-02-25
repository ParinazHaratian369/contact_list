from customtkinter import *
import json
from tkinter import messagebox as mb
import re
from tkinter import ttk

# ---------------Handle Database-----------------
def database_handler(path):
    try:
        with open(path, 'r') as f:
            database = json.load(f)
    except:
        database={}
        with open(path, 'w') as f:
            json.dump(database, f, indent=4)

    return database

path = "contacts.json"
contacts = database_handler(path)

# ---------------Utility Functions---------------
def calculate_size(percent, total):
     return int((percent / 100) * total)

def clear_widgets(parent):
    for widget in parent.winfo_children():
        widget.destroy()

def save_contacts():
    with open(path, "w") as f:
        json.dump(contacts, f, indent=4)  

def populate_table(filter_name=""):
    pass

# ---------------Main Functions------------------
def is_valid_email(email_address):
    pattern = r"^[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[a-z]+$"
    return bool(re.match(pattern, email_address))

def submit_contact(name, phone , email, address):
    contact_name = name.get()
    phone_number = phone.get()
    email_address = email.get()
    city = address.get()

    if not contact_name or not phone_number or not email_address or not city:
        mb.showerror("Empty Field", "All fields must be filled!")
        return

    if contact_name not in contacts:
        if contact_name.isalpha():
            if phone_number.isnumeric():
                if is_valid_email(email_address):
                    if city.isalpha():
                        contacts.update({
                            contact_name:{
                                'phone': phone_number,
                                'email': email_address,
                                'address': city
                            }
                        })

                        save_contacts()
                        mb.showinfo("Success", "Contact added successfully")
                    else:
                        mb.showerror("Incorrect Format", "Invalid city; It should be a string")
                else:
                    mb.showerror("Incorrect Format", "Invalid adderss; ex.parinaz@gmail.com")
            else:
                mb.showerror("Incorrect Format", "Invalid phone number")
        else:
            mb.showerror("Invalid Format", "Invalid contact name")
    else:
        mb.showerror("Error", "Contact Already Exists!")
    print(contacts)



def show_add_contact():
    clear_widgets(central_frame)

    CTkLabel(central_frame, text='Add Contact', font=('Arial Bold', 30)).pack(pady=calculate_size(4, height))

    bordered_frame = CTkFrame(central_frame, corner_radius=10, border_width=2)
    bordered_frame.pack(padx=calculate_size(3, width), pady=calculate_size(3, height), fill='both', expand=False)

    entry_width = calculate_size(50, width)
    label_width = calculate_size(15, width)
    row_padding = calculate_size(2, height)

    form_frame = CTkFrame(bordered_frame, border_width=2)
    form_frame.pack(padx=row_padding, pady=row_padding, fill='both', expand=False)

    entries_data = ["Contact Name *", "Phone *", "Email", "Address"]
    entry_widgets={}

    for index, label in enumerate(entries_data):

        CTkLabel(form_frame ,text=f"{label}", width=label_width).grid(row=index, column=0, padx=row_padding, pady=row_padding, sticky='w')

        entry = CTkEntry(form_frame, placeholder_text=f"{label}", width=entry_width, height=calculate_size(6, height))
        entry.grid(row=index, column=1, padx=row_padding, pady=row_padding, sticky='w')

        entry_widgets[label]=entry

    CTkButton(form_frame,
              text="Add Contact",
             corner_radius=10,
             command=lambda:submit_contact(entry_widgets["Contact Name *"],
                                           entry_widgets["Phone *"], 
                                           entry_widgets["Email"], 
                                           entry_widgets["Address"])
                                           ).grid(row=4, column=1, padx=row_padding, pady=row_padding, sticky='e')
 
def search_contact(name):
    populate_table(name)

def create_table(table_frame):
    global table

    table = ttk.Treeview(table_frame, columns=("name", "phone", "email", "address"), show="headings", height=15)
    
    table.heading("name", text="Contact Name")
    table.heading("phone", text="Phone Number")
    table.heading("email", text="Email Address")
    table.heading("address", text="City")
    table.column("name", width=calculate_size(15, width))
    table.column("phone", width=calculate_size(15, width))
    table.column("email", width=calculate_size(20, width))
    table.column("address", width=calculate_size(10, width))

    table.pack(fill="both")

def show_manage_db():
    # clear central frame
    clear_widgets(central_frame)

    # add Manage DB label
    CTkLabel(central_frame, text="ManageDB", font=("Arial", 30)).pack(pady=calculate_size(2, height))

    # defining bordered_frame
    bordered_frame = CTkFrame(central_frame)
    bordered_frame.pack(padx=calculate_size(3, height), pady=calculate_size(2, height), fill="both", expand=False)

    # defining search_frame
    search_frame = CTkFrame(bordered_frame)
    search_frame.pack(padx=calculate_size(2, height), pady=calculate_size(2, height), fill="x")

    # defining an entry to search a contact member
    search_entry = CTkEntry(search_frame, placeholder_text="Search Name", width=calculate_size(25, width))
    search_entry.pack(side="left")

    # search button
    CTkButton(search_frame, text="Search", command=lambda: search_contact(search_entry.get())).pack(side="right")

    # defining table_frame
    table_frame = CTkFrame(bordered_frame)
    table_frame.pack(padx=calculate_size(2, height), pady=calculate_size(1, height), fill="x", expand=False)

    # creating the table
    create_table(table_frame)



# ---------------Initial Functions---------------
def show_empty_state():
    CTkLabel(central_frame,
             text="Empty. Pick an action, (ex:Add contact or Manage DB)",
             font=("Arial",20),
             text_color="gray").pack(expand=True)

def create_side_button(text, command):
    button = CTkButton(sidebar_frame,
              text=text,
              width=sidebar_width,
              height=calculate_size(8, height),
              corner_radius=0,
              command=command).pack()
    return button

def add_sidebar_buttons():
    create_side_button("Add Contact", show_add_contact)
    create_side_button("Manage DB", show_manage_db)

# ---------------Application Theme---------------
set_appearance_mode("system")
set_default_color_theme("breeze.json")

# ----------------Setup-------------------
window = CTk()
window.title("Contact List App")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

width = int(screen_width * .7)
height = int(screen_height * .7)

x = ((screen_width // 2) - (width // 2))
y = ((screen_height // 2) - (height // 2))

window.geometry(f"{width}x{height}+{x}+{y}")

sidebar_width = calculate_size(20, width)
sidebar_frame = CTkFrame(window, width=sidebar_width, corner_radius=0)
sidebar_frame.pack(side='left', fill='y')

CTkLabel(sidebar_frame, text="Manage DB", width=sidebar_width, font=("Arial", 28)).pack(pady=calculate_size(2, height))

add_sidebar_buttons()

central_frame = CTkFrame(window, corner_radius=0)
central_frame.pack(side="left",fill="both",expand=True)

show_empty_state()

window.mainloop()