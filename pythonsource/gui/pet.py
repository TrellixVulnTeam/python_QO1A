# 좋아하는 동물 투표하는 프로그램
from tkinter import *

def imgView():
    if rdo.get() == 1:
        photo = PhotoImage(file="./resource/dog2.gif")
        label2.configure(image=photo)
    elif rdo.get() == 2:
        photo = PhotoImage(file="./resource/cat2.gif")
        label2.configure(image=photo)
    elif rdo.get() == 3:
        photo = PhotoImage(file="./resource/rabbit.gif")
        label2.configure(image=photo)

window = Tk()
window.title("애완동물 선택하기")
window.geometry("400x500")
label1 = Label(window, text="좋아하는 동물 투표", font=("궁서체",27), fg="red")

rdo = IntVar()
rb1 = Radiobutton(window, text="강아지", variable=rdo, value=1)
rb2 = Radiobutton(window, text="고양이", variable=rdo, value=2)
rb3 = Radiobutton(window, text="토끼", variable=rdo, value=3)

btn = Button(window, text="사진 보기", command=imgView)

label2 = Label(window, text=" ")

label1.pack()
rb1.pack()
rb2.pack()
rb3.pack()
btn.pack()
label2.pack()

window.mainloop()
