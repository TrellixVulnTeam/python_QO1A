from tkinter import *

window = Tk()
window.title("이미지 버튼 배치")

# 내코딩 망!
# img_path = ["./resource/instagram.png", "./resource/facebook.png", "./resource/twitter.png"]

# for i in range(3):
#     photo = PhotoImage(file=img_path[i])
#     btn = Button(window, image=photo)
#     btn.pack(side=LEFT, fill=x, ipadx=10, ipady=10)

# 쌤코딩
potoList = [
    PhotoImage(file="./resource/instagram.png"),
    PhotoImage(file="./resource/facebook.png"),
    PhotoImage(file="./resource/twitter.png"),
]

btnList = []

for i in range(3):
    button = Button(window, image=None)
    btnList.append(button)

for i, button in enumerate(btnList):
    button.configure(image=potoList[i])
    button.pack(side=LEFT, fill=X, ipadx=10, ipady=10)

window.mainloop()
