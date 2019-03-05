#!/usr/bin/python3
from tkinter import *

'''
# 事件绑定 #
'''


root = Tk()
root.title('事件绑定')

root.minsize(300,300)

# ---------------------------鼠标事件--------------------------- #
"""
# 鼠标点击操作
'''
btn1 = Button(root,text='按钮1')

def one(evt) :
    print('左键')

def two(evt) :
    print('右键')

def thr(evt) :
    print('中键')

# 鼠标左键
btn1.bind('<Button-1>',one)
# 鼠标右键
btn1.bind('<Button-2>',two)
# 鼠标中键
btn1.bind('<Button-3>',thr)
'''

# 鼠标移入操作
'''
btn1 = Button(root,text = '按钮1')

def mouse_in(evt) :
    print('鼠标进入')
    btn1['bg'] = 'pack'

def mouse_out(evt) :
    print('鼠标离开')
    btn1['bg'] = 'white'

# 鼠标进入
btn1.bind('<Enter>',mouse_in)
# 鼠标离开
btn1.bind('<Leave>',mouse_out)
'''

btn1.grid(row=0,column=0)
"""

# ---------------------------键盘事件--------------------------- #

# 输入框 绑定操作
entry = Entry(root)

def one(evt) :
    print('a')
    print(evt.widget)
def two(evt) :
    print('AAA')

entry.bind('<KeyPress-a>',one)
entry.bind('<Lock-KeyPress-A>',two)

entry.grid()


root.mainloop()
