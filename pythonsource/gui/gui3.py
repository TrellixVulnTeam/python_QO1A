from tkinter import *

window = Tk()

photo = PhotoImage(file="./resource/cat2.gif")
label = Label(window, image=photo)

label.pack()
window.mainloop()
