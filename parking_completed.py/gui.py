from tkinter import *
from tkinter import messagebox as msg

window = Tk()
window.title("parking")
window.geometry("500x500")

window.configure(bg= "peach puff")
Label(window, text="Name:", bg= "peach puff", fg= "dim gray", font= ("georgia", 18)).place(x=15, y=10)
Label(window, text="Model:", bg= "peach puff", fg= "dim gray", font= ("georgia", 18)).place(x=15, y=10)
Label(window, text="Color:", bg= "peach puff", fg= "dim gray", font= ("georgia", 18)).place(x=15, y=10)
Label(window, text="Plate:", bg= "peach puff", fg= "dim gray", font= ("georgia", 18)).place(x=15, y=10)


window.mainloop()