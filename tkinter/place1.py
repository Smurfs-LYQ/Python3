#!/usr/bin/python3

import tkinter

root = tkinter.Tk()

root.minsize(400,400)

btn1 = tkinter.Button(root, text='按钮1')
btn1.place(x = 10, y = 10)
# x 设置按钮的x坐标
# y 设置按钮的y坐标
# width 设置按钮的宽
# height 设置按钮的高

btn2 = tkinter.Button(root, text='按钮2')
btn2.place(x = 10, y = 40)

root.mainloop()
