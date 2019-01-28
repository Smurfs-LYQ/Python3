#!/usr/bin/python3

import tkinter

# 创建一个Tk窗口
root = tkinter.Tk()

# 设置界面的最小值
root.minsize(300,300)

btn1 = tkinter.Button(root, text='test1')
btn1.pack()

btn2 = tkinter.Button(root, text='test2')
btn2.pack(side='bottom')

# 保持主窗口一直在消息循环中...
root.mainloop()
