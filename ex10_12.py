from tkinter import *
from tkinter import messagebox
from time import *
import random

window=Tk()
btnList=[None]*9

fnameList=["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif", ]
#random.shuffle(fnameList)
num = 0

def clickNext():
    global num,  photo, pLabel, fLabel
    num += 1
    if num>8:
        num = 0
    photo=PhotoImage(file="h:/gif/"+fnameList[num])
    pLabel.configure(image=photo)
    fLabel.configure(text=fnameList[num])
    #pLabel.image=photo #pLabel을 global로 선언하면 이 줄은 없어도 됨

def clickPrev():
    global num,  photo, pLabel, fLabel
    num -= 1
    if num<0:
        num = 8
    photo=PhotoImage(file="h:/gif/"+fnameList[num])
    pLabel.configure(image=photo)
    fLabel.configure(text=fnameList[num])
    #pLabel.image=photo #pLabel을 global로 선언하면 이 줄은 없어도 됨

window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext=Button(window, text=">> 다음", command=clickNext)
fLabel=Label(window, text=fnameList[num])

photo=PhotoImage(file="h:/gif/"+fnameList[0])
pLabel=Label(window, image=photo)
btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)
fLabel.place(x=330, y=12)

window.mainloop()
