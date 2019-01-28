#!/usr/bin/python3

import tkinter

# 创建主窗口
root = tkinter.Tk()

# 设置主窗口大小
root.minsize(300,300)

# 添加组件
btn1 = tkinter.Button(root, text='text1')
btn1.grid()

# 保持主窗口一直在消息循环
root.mainloop()
