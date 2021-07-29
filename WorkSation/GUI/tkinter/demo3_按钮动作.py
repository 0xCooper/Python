#添加按钮与按钮动作
from tkinter import *
 
window = Tk()
window.title("First Window")
window.geometry("350x200")
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
 
def clicked():
    btn.configure(bg="blue") #设置点击动作后标签变化
    lbl.configure(text="Button was clicked!")
 
btn = Button(window, text="Click Me", bg="orange", fg="red",command=clicked)#设置点击动作和其他属性
btn.grid(column=1, row=0)
window.mainloop()