#!/usr/bin/python3
from tkinter import *

'''
# 事件绑定 #
'''


root = Tk()
root.title('事件绑定')

root.minsize(300,300)

# 鼠标点击操作
'''
btn1 = Button(root,text='按钮1')

def one(evt) :
    print('左键')

def two(evt) :
    print('右键')

<<<<<<< HEAD
def thr(evt) :
    print('中键')

# 鼠标左键
btn1.bind('<Button-1>',one)
# 鼠标右键
btn1.bind('<Button-2>',two)
# 鼠标中键
btn1.bind('<Button-3>',thr)
'''

# 鼠标进入操作
btn1 = Button(root,text = '按钮1')

def mouse_in(evt) :
    print('鼠标进入')

def mouse_out(evt) :
    print('鼠标离开')

# 鼠标进入
btn1.bind('<Enter>',mouse_in)
# 鼠标离开
btn1.bind('<Leave>',mouse_out)
=======
btn1.bind('<Button-3>',one)
>>>>>>> 818b678995f806db56d219c7e4a18b88b999396c

btn1.grid(row=0,column=0)

root.mainloop()
