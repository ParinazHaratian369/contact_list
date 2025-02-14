from customtkinter import *

# ---------------Utility Functions---------------
def calculate_size(percent, total):
     return int((percent / 100) * total)

# ---------------Main Functions------------------
def show_add_contact():
    pass

# ---------------Initial Functions---------------
def show_empty_state():
    CTkLabel(central_frame,
             text="Empty. Pick an action, (ex:Add contact or Manage DB)",
             font=("Arial",20),
             text_color="gray").pack(expand=True)

def create_nav_button(text, command):
    button = CTkButton(navbar_frame,
              text=text,
              width=navbar_width,
              height=calculate_size(8, height),
              corner_radius=0,
              command=command).pack()
    return button

def add_navbar_buttons():
    create_nav_button("Add Contact", show_add_contact)
    # create_nav_button("Manage DB", show_manage_db)

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

navbar_width = calculate_size(20, width)
navbar_frame = CTkFrame(window, width=navbar_width, corner_radius=0)
navbar_frame.pack(side='left', fill='y')

CTkLabel(navbar_frame, text="Manage DB", width=navbar_width, font=("Arial", 28)).pack(pady=calculate_size(2, height))

add_navbar_buttons()

central_frame = CTkFrame(window, corner_radius=0)
central_frame.pack(side="left",fill="both",expand=True)

show_empty_state()

window.mainloop()