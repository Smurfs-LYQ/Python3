#!/usr/bin/python3

import tkinter

root = tkinter.Tk()

root.minsize(300,300)

btn1 = tkinter.Button(root, text='text1')
btn1.pack(fill = 'x')

btn2 = tkinter.Button(root, text='text1')
btn2.pack(anchor = 'w')

root.mainloop()
