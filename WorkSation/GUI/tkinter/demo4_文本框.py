#添加文本框
from tkinter import *
import tkinter
 
window = Tk()
window.title("First Window")
window.geometry("500x500")
photo = tkinter.PhotoImage(file="/home/makapaka/Pictures/动漫/code.png")#file：t图片路径
lbl = Label(window, text="Hello",image=photo,compound = tkinter.CENTER
,font=("华文行楷",20),#字体和字号
fg = "white")#前景色)#关键:设置为背景图片

lbl.grid(column=0, row=0)
txt = Entry(window, width=10)  #文本框
txt.grid(column=1, row=0)
def clicked():
    res = "Welcome to " + txt.get()#get()函数获取输入框的值
    lbl.configure(text=res)
# txt.focus()#设置文本焦点


btn = Button(window, text="Click Me",command=clicked)
btn.grid(column=2, row=0)
window.mainloop()