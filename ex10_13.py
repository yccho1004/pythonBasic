from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox

def func_open():
    filename=askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo1 = PhotoImage(file=filename)
    photo2 = PhotoImage(file=filename)
    for i in range(0, photo2.width()):
        for j in range(0, photo2.height()):
            (r, g, b) = photo2.get(i, j)
            grayscale = int((r+g+b)/3)
            photo2.put("#%02x%02x%02x" %(grayscale, grayscale, grayscale), (i, j))
    pLabel1.configure(image=photo1)
    pLabel1.image=photo1
    pLabel2.configure(image=photo2)
    pLabel2.image=photo2

def func_exit():
    messagebox.showinfo("파일 종료","프로그램 종료")

window = Tk()
window.title("명화 감상하기")
photo1=PhotoImage()
photo2=PhotoImage()
pLabel1=Label(window, image=photo1)
pLabel1.pack(expand=True, side=LEFT)
pLabel2=Label(window, image=photo2)
pLabel2.pack(expand=True, side=LEFT)

mainMenu=Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", accelerator="Ctrl+F", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", accelerator="Ctrl+X", command=func_exit)
window.bind("<Control-f>", func_open)
window.bind("<Control-x>", func_exit)
window.mainloop()

