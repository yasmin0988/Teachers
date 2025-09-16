from tkinter import *
from tkinter import messagebox as msg

window = Tk()
window.title("Parking App")
window.geometry("600x400")
window.configure(bg="peach puff")

name = StringVar()
model = StringVar()
color = StringVar()
plate = StringVar()

label_style = {"bg": "peach puff", "fg": "dim gray", "font": ("georgia", 14)}
entry_style = {"font": ("Arial", 12), "width": 25}

Label(window, text="Name:", **label_style).place(x=30, y=30)
name_entry = Entry(window, textvariable=name, **entry_style)
name_entry.place(x=150, y=30)

Label(window, text="Model:", **label_style).place(x=30, y=70)
model_entry = Entry(window, textvariable=model, **entry_style)
model_entry.place(x=150, y=70)

Label(window, text="Color:", **label_style).place(x=30, y=110)
color_entry = Entry(window, textvariable=color, **entry_style)
color_entry.place(x=150, y=110)

Label(window, text="Plate:", **label_style).place(x=30, y=150)
plate_entry = Entry(window, textvariable=plate, **entry_style)
plate_entry.place(x=150, y=150)


window.mainloop()