from tkinter import *
from tkinter import messagebox

def clickMouse(event):
    txt = ""
    if event.num == 1:
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num == 3:
        txt += "마우스 오른쪽 버튼이 ("
    txt += str(event.y)+","+str(event.x)+")에서 출력됨"
    label1.configure(text = txt)

window = Tk()
window.geometry("400x400")
window.bind("<Button>", clickMouse)

label1 = Label(window, text="이 곳이 바뀜")
label1.pack(expand=True, anchor=CENTER)

window.mainloop()

