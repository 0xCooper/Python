from tkinter import *
 

 
window = Tk()
window.title("First Window")
window.geometry("350x200")   #设置窗口大小
lbl = Label(window, text="Hello")#标签
lbl.grid(column=0, row=0)#标签位置
btn = Button(window, text="Click Me")#按钮
btn.grid(column=1, row=0)#按钮位置
window.mainloop()