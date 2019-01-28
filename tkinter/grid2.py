#!/usr/bin/python3

import tkinter

# 创建主窗口
root = tkinter.Tk()

# 设置主窗口大小
root.minsize(300,300)

# 添加组件
btn1 = tkinter.Button(root, text='text1')
btn1.grid(row = 0,column=0)
# row    行
# column 列

btn2 = tkinter.Button(root, text='text2')
# btn2.grid()
btn2.grid(row = 0,column=1)

btn3 = tkinter.Button(root, text='text3')
# btn3.grid()
btn3.grid(row = 0,column=2)

# 保持主窗口一直在消息循环
root.mainloop()
