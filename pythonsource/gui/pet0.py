# 좋아하는 동물 투표하는 프로그램
from tkinter import *


def view():
    click_rdo = rdo_value.get()
    if click_rdo == 1:
        img_label.configure(image=photo1)
    elif click_rdo == 2:
        img_label.configure(image=photo2)
    else:
        img_label.configure(image=photo3)


window = Tk()
window.geometry("500x400")
title = Label(window, text="좋아하는 동물 투표", font=("궁서체", 30), fg="red")

rdo_value = IntVar()

rdo_dog = Radiobutton(window, text="강아지", variable=rdo_value, value=1)
rdo_cat = Radiobutton(window, text="고양이", variable=rdo_value, value=2)
rdo_rabbit = Radiobutton(window, text="토끼", variable=rdo_value, value=3)

photo1 = PhotoImage(file="./resource/dog2.gif")
photo2 = PhotoImage(file="./resource/cat2.gif")
photo3 = PhotoImage(file="./resource/rabbit.gif")

button = Button(window, text="사진보기", command=view)
img_label = Label(window, image=None)


title.pack()
rdo_dog.pack()
rdo_cat.pack()
rdo_rabbit.pack()
button.pack()
img_label.pack()
window.mainloop()
