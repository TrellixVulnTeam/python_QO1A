from tkinter import *
from tkinter.filedialog import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("400x400")
window.title("명화감상")

def file_open():
    fileName = askopenfilename(
        parent = window,
        filetypes=(
            ("gif 파일","*.gif"),
            ("jpg 파일","*.jpg *.jpeg"),
            ("모든 파일","*.*"),
        ),
    )
    photo = ImageTk.PhotoImage(file=fileName)   # ImageTk는 PIL의 PhotoImage
    # 아래 코드 둘 다 있어야 가능
    image_label.configure(image=photo)
    image_label.image = photo   # 함수가 끝나고도 유지되도록


# 메뉴 생성
mainMenu = Menu(window)
# 메뉴 안에 들어갈 메뉴 생성
fileMenu = Menu(mainMenu)

# 메뉴 붙이기
window.config(menu = mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)

fileMenu.add_command(label="열기", command=file_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=quit)

# 이미지 보여줄 라벨
image_label = Label(window, image=None)
image_label.pack(expand=1, anchor=CENTER)

window.mainloop()
