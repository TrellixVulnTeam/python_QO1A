# 마우스 이벤트
from tkinter import *
from tkinter import messagebox

def clickLeft(event):
    messagebox.showinfo("이벤트", "마우스 왼쪽 버튼 클릭")
    

window = Tk()
window.title("마우스 이벤트")
window.bind("<Button-1>", clickLeft)
window.mainloop()
