from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("클릭", "강아지가 귀엽죠?")

window = Tk()
photo = PhotoImage(file="./resource/dog2.gif")
button1 = Button(window, image=photo, command=myFunc)

button1.pack()
window.mainloop()
