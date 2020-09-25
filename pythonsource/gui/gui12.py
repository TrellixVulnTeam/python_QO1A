# 위젯배치 : place()함수 사용
from tkinter import *

btnList = [None] * 9
print(btnList)

nameList = [
    "eclair.gif",
    "froyo.gif",
    "gingerbread.gif",
    "honeycomb.gif",
    "icecream.gif",
    "jellybean.gif",
    "kitkat.gif",
    "lollipop.gif",
    "marshmallow.gif",
]
photoList = [None] * 9


xPos, yPos = 0,0
num = 0

window = Tk()
window.title("안드로이드 버전")
window.geometry("210x210")

for i in range(0,9):
    photoList[i] = PhotoImage(file="./resource/" + nameList[i])
    btnList[i] = Button(window, image=photoList[i])

# 위젯 배치
for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70
window.mainloop()


