from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("First Window")
window.geometry("350x200")
lbl = Label(window, text="Hello world")
lbl.grid(column=0, row=0)

combo = Combobox(window)
combo['values'] = (1,2,3,4,5,"Text")
combo.current(1)
combo.grid(column=0, row=1)

def clicked():
    data=combo.get()
    lbl.configure(text=data)
btn = Button(window, text="Click Me",command=clicked)
btn.grid(column=0, row=3)

window.mainloop()