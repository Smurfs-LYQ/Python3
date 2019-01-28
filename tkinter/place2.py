#!/usr/bin/python3

import tkinter

root = tkinter.Tk()

root.minsize(400,400)

btn1 = tkinter.Button(root, text='按钮1')
btn1.place(relx = 0.1, rely = 0.1)
# relx 设置按钮的x坐标(百分之比例 0.1 = 10%)
# rely 设置按钮的y坐标(百分之比例 0.1 = 10%)
# relwidth 设置按钮的长(百分之比例 0.1 = 10%)
# relheight 设置按钮的高(百分之比例 0.1 = 10%)

btn2 = tkinter.Button(root, text='按钮2')
btn2.place(relx = 0.1, rely = 0.2, relwidth = 0.2, relheight = 0.3)

root.mainloop()
