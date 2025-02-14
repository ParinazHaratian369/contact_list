from customtkinter import *

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


window.mainloop()