from tkinter import *  
  
root = Tk()  
  
root.geometry("200x200")  
  
def open():  
    top = Toplevel(root)  
    top2= Toplevel(root)  
    top.mainloop()
    top2.mainloop()  
  
btn = Button(root, text = "open", command = open)  
  
btn.place(x=72.5,y=0.5)  
  
root.mainloop()