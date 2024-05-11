"""
This is an image viewing app using tkinter.
In this app, you can view images in a given folder.
"""

from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.geometry("600x400")
root.title('Image Viewer')
root.maxsize(600, 630)
root.minsize(600, 630)


def forward():
    global imgList
    global label
    global index
    global image
    index += 1
    if index == len(imgList):
        index = 1
    image = ImageTk.PhotoImage(Image.open(f"Your-folder-name/{imgList[index]}").resize((600, 550)))
    label = Label(image=image)
    label.grid(row=0, column=0, columnspan=2)
    status.config(text=f"Image {index + 1} of {len(imgList)}", borderwidth=1, pady=1)


def back():
    global label
    global index
    global image
    index -= 1
    if index == 0:
        index = -1
    image = ImageTk.PhotoImage(Image.open(f"Your-folder-name/{imgList[index]}").resize((600, 550)))
    label = Label(image=image)
    label.grid(row=0, column=0, columnspan=2)
    status.config(text=f"Image {index} of {len(imgList)}", borderwidth=1, pady=1)


imgList = os.listdir("Your-folder-path")
image = ImageTk.PhotoImage(Image.open(f"Your-folder-name/{imgList[1]}").resize((600, 550)))
index = 0
status = Label(text=f"Image {index + 1} of {len(imgList)}", borderwidth=1, pady=1)

label = Label(image=image)
label.grid(row=0, column=0, columnspan=2)

buttonBack = Button(text="<<", font="lucida 14 bold", command=back)
buttonForward = Button(text=">>", font="lucida 14 bold", command=forward)

buttonForward.grid(row=1, column=1)
buttonBack.grid(row=1, column=0)

status.grid(row=2, column=0, columnspan=3, )

root.mainloop()
