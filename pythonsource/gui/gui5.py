from tkinter import *

def test():
    pass

window = Tk()
window.title("버튼")

btn = Button(window, text="종료", fg="red", command=test)
btn.pack()
window.mainloop()
