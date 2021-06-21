from tkinter import*
from tkinter import messagebox

colors = ["blue", "purple", "pink"]

def select():
    messagebox.showinfo("your choice", colors[PICKED_COLOR.get()-1])

window = Tk()
window.title("colorpicking")
windoq=window.geometry('560x280')

Label(text="pick a color", padx=15, pady = 10).grid(row=0, column = 0, sticky=W)
    
PICKED_COLOR = IntVar()

valRow = 1

for color in colors:
    Radiobutton(text=color, value=valRow, variable=PICKED_COLOR, padx=15, pady = 20, command = select).grid(row=valRow, sticky=W)
    valRow += 1

window.mainloop()