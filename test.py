from os import path
import os
from tkinter import *
from tkinter.filedialog import askopenfilename

pwd = os.getcwd()

def selectPath():
    path_ = askopenfilename()
    path.set(path_)



# def savepath():
#     path_ = askopenfilename()
#     save = path.set(path_)



def fanbianyi():
    os.system("node"+" "+pwd+"\wxappUnpacker-master\wuWxapkg.js"+" "+ path.get())
    # print(path.get()[:-7])


root = Tk()
path = StringVar()


Label(root, text="目标路径").grid(row=0, column=0)
Entry(root, textvariable=path).grid(row=0, column=1)
Button(root, text="文件路径", command=selectPath).grid(row=0, column=2)
# Label(root, text="保存").grid(row=1, column=0)
# Entry(root, textvariable=save).grid(row=1, column=1)
# Button(root, text="保存路径", command=selectPath).grid(row=1, column=2)
Button(root, text="确定", command=fanbianyi).grid(row=2, column=1)


root.mainloop()

