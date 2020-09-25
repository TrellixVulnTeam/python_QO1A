from tkinter import *
from tkinter import messagebox

def mouse_click(event):
    txt = ""
    if event.num == 1:
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num == 3:
        txt += "마우스 오른쪽 버튼이 ("
    txt += str(event.x) + "," + str(event.y) + ") 에서 클릭됨"
    label.configure(text=txt)


window = Tk()
window.title("마우스 이벤트")
window.geometry("400x400")
window.bind("<Button>", mouse_click)
label = Label(window, text=None)
label.pack()
window.mainloop()
