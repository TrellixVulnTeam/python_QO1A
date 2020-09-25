from tkinter import *

window = Tk()
window.title("버튼")

btn = Button(window, text="종료", fg="red", command=quit)
btn.pack()
window.mainloop()

