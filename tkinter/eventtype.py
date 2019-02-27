#!/usr/bin/python3
from tkinter import *

'''
# 事件绑定 #
'''


root = Tk()
root.title('事件绑定')

root.minsize(300,300)

btn1 = Button(root,text='按钮1')

def one(evt) :
    print('123')

btn1.bind('<Button-3>',one)

btn1.grid(row=0,column=0)

root.mainloop()

#测试一下可不可以
