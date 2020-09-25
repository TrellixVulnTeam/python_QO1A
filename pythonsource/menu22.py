from tkinter import *
from tkinter.simpledialog import *


def num_input():
    value = askinteger("주사위", "주사위 숫자(1~6)를 입력하세요", minvalue=1, maxvalue=6)
    label.configure(text=str(value))


window = Tk()
window.geometry("400x400")

# 메뉴 담을 공간 생성
mainMenu = Menu(window)
window.config(menu=mainMenu)

# 메뉴 생성
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
# 서브 메뉴 생성
fileMenu.add_command(label="입력", command=num_input)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=quit)


label = Label(window, text=None)
label.pack()
window.mainloop()
