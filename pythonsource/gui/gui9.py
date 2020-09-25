from tkinter import *

def myFunc():
    if rdo.get() == 1:
        label.configure(text="파이썬")
    elif rdo.get() == 2:
        label.configure(text="Java")
    else:
        label.configure(text="C++")

window = Tk()

rdo = IntVar()
rb1 = Radiobutton(window, text="파이썬", variable=rdo, value=1, command=myFunc)
rb2 = Radiobutton(window, text="Java", variable=rdo, value=2, command=myFunc)
rb3 = Radiobutton(window, text="C++", variable=rdo, value=3, command=myFunc)

label = Label(window, text="선택한 언어 : ", fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
label.pack()
window.mainloop()
