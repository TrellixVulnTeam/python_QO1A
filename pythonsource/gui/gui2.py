from tkinter import *

window = Tk()
window.title("라벨생성")

label1 = Label(window, text="파이썬을...")
label2 = Label(window, text="열심히", font=("궁서체",30),fg="blue")
label3 = Label(window, text="공부 중입니다", bg="magenta", width=20, height=5, anchor=SE)

# 위젯 배치
label1.pack()
label2.pack()
label3.pack()

window.mainloop()
