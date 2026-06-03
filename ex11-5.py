from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

def loadImage(fname):
    global inImage, sizeWidth, sizeHeight
    with open(fname, "rb") as inFp:
        for row in range(0, sizeHeight):
            tmpList = []
            for col in range(0, sizeWidth):
                data = int(ord(inFp.read(1)))
                tmpList.append(data)
            inImage.append(tmpList)

def displayImage(image):
    global sizeWidth, sizeHeight
    rgbString = ""
    for row in range(0, sizeHeight):
        tmpString = ""
        for col in range(0, sizeWidth):
            data = image[row][col]
            tmpString += "#%02x%02x%02x " %(data, data, data)
        rgbString += "{"  + tmpString + "} "
    paper.put(rgbString)

def displayImage2(image):
    global sizeWidth, sizeHeight
    rgbString = ""
    for row in range(0, sizeHeight):
        tmpString = ""
        for col in range(0, sizeWidth):
            data = image[row][col]
            paper.put("#%02x%02x%02x " %(data, data, data), (col, row))

def fileopen():
    fname = askopenfilename(parent=window, filetypes = (("Raw 파일", "*.raw"), ("모든 파일","*.*")))
    return fname

def inputSize():
    sw = askinteger("Image Width", "이미지 폭을 입력하세요")
    sh = askinteger("Image Height", "이미지 높이를 입력하세요")
    return sw, sh

window = None
canvus = None
sizeWidth, sizeHeight = 0, 0
filename = ""
inImage = []

window = Tk()
window.title("흑백 사진 보기")

filename = fileopen()
sizeWidth, sizeHeight = inputSize()

canvas = Canvas(window, height = sizeHeight, width = sizeWidth)
paper = PhotoImage(width = sizeWidth, height = sizeHeight)
canvas.create_image((sizeWidth/2, sizeHeight/2), image = paper, state = 'normal')

loadImage(filename)
displayImage2(inImage)

canvas.pack()
window.mainloop()
