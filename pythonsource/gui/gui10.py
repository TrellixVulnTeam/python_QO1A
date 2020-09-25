# 위젯 배치
from tkinter import *

window = Tk()

for i in range(3):
    btn = Button(window, text="버튼" + str(i + 1))
    btn.pack(side=LEFT)  # pack도 가능

# btn1 = Button(window, text="버튼1")
# btn2 = Button(window, text="버튼2")
# btn3 = Button(window, text="버튼3")

# btn1.pack(side=RIGHT)
# btn2.pack(side=RIGHT)
# btn3.pack(side=RIGHT)

# fill : 채우기
# padx, pady : 바깥쪽 여백
# ipadx, ipady : 안쪽 여백
# btn1.pack(side=BOTTOM, fill=X, padx=10, pady=10)
# btn2.pack(side=BOTTOM, ipadx=10, ipady=10)   # i 붙이면 안쪽 padding
# btn3.pack(side=BOTTOM)

window.mainloop()
