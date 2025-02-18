from customtkinter import *

# ---------------Utility Functions---------------
def calculate_size(percent, total):
     return int((percent / 100) * total)

def clear_widgets(parent):
    for widget in parent.winfo_children():
        widget.destroy()

# ---------------Main Functions------------------
def show_add_contact():
    clear_widgets(central_frame)

    CTkLabel(central_frame, text='Add Contact', font=('Arial Bold', 30)).pack(pady=calculate_size(4, height))

    bordered_frame = CTkFrame(central_frame, corner_radius=10, border_width=2)
    bordered_frame.pack(padx=calculate_size(3, width), pady=calculate_size(3, height), fill='both', expand=False)
    






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

sidebar_width = calculate_size(20, width)
sidebar_frame = CTkFrame(window, width=sidebar_width, corner_radius=0)
sidebar_frame.pack(side='left', fill='y')

CTkLabel(sidebar_frame, text="Manage DB", width=sidebar_width, font=("Arial", 28)).pack(pady=calculate_size(2, height))

add_sidebar_buttons()

central_frame = CTkFrame(window, corner_radius=0)
central_frame.pack(side="left",fill="both",expand=True)

show_empty_state()

window.mainloop()