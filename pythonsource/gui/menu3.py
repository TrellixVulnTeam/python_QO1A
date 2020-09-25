from tkinter import *
from tkinter.filedialog import *

def file_input():
    fName = askopenfilename(parent=window, filetypes=(("gif파일",".gif"), ("모든파일", "*.*"))
    )
    label.configure(text=fName)

window = Tk()
window.geometry("400x400")

# 메뉴 담을 공간 생성
mainMenu = Menu(window)
window.config(menu=mainMenu)

# 메뉴 생성
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
# 서브 메뉴 생성
fileMenu.add_command(label="열기", command=file_input)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=quit)

label = Label(window, text=None)
label.pack()
window.mainloop()
