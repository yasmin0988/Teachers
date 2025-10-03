from tkinter import *

win = Tk()
win.title("Calculator")
win.geometry("300x400")
win.configure(bg="light goldenrod")

result = StringVar()
Entry(win, width=17, textvariable=result, font=("georgia", 18), state="readonly").place(x=25, y=20)

def click(value):
    if value == "=":
        total = str(eval(result.get()))
        result.set(total)
    
    else:
        given = result.get()
        result.set(given + value)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

dist_x = 70
dist_y = 70

for row in range(4):
    for clmn in range(4):
        text = buttons[row][clmn]
        Button(win, text=buttons[row][clmn], width=3, font=("georgia", 16),
                bg = "lemon chiffon", command=lambda t=text: click(t)).place(x=25 + clmn *dist_x, y=90 + row * dist_y)

win.mainloop()