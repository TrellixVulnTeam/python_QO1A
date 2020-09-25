from tkinter import *
from tkinter.filedialog import *
from PIL import Image, ImageTk

def file_open():
    fName = askopenfilename(
        parent=window, 
        filetypes=(
            ("gif파일","*.gif"),
            ("jpg파일","*.jpg *.jpeg"),
            ("모든파일","*.*"),
        ),
    )
    photo = ImageTk.PhotoImage(Image.open(fName))
    label.configure(image=photo)
    label.image = photo


window = Tk()
button = Button(window, text="이미지 보기", command=file_open)
label = Label(window, image=None)

button.pack()
label.pack()
window.mainloop()
