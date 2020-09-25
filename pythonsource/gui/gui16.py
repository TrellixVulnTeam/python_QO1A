from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    messagebox.showinfo("키보드이벤트","입력 키 :"+chr(event.keycode))
# chr() : 아스키 코드 값을 받아서 그 코드에 해당하는 문자 출력
# ord() : 문자의 아스키 코드 값을 돌려주는 함수

window = Tk()
window.geometry("200x200")
window.bind("<Key>", keyEvent)
window.mainloop()
