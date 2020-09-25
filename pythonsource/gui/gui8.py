from tkinter import *
from tkinter import messagebox

def myFunc():
    if chkvalue.get() == 0:
        messagebox.showinfo("","체크 버튼이 꺼졌어요")
    else:
        messagebox.showinfo("","체크 버튼이 켜졌어요")

window = Tk()

chkvalue = IntVar() # check 됐는지 int값으로 받겠다
chk1 = Checkbutton(window, text="클릭하세요", variable=chkvalue, command=myFunc)

chk1.pack()
window.mainloop()
