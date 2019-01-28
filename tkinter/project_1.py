#!/usr/bin/python3

from tkinter import *

# 创建一个窗口
root = Tk()

# 设置窗口的最小大小
root.minsize(300,250)

# 存储当前操作步骤
lists = []
# 标记当前是否按下了运算符按钮
signflag = False
# 标记当前显示的是否为运算结果
res = False

# 定义清空操作
def clear() :
    val.set('0')

# 数字按钮操作
def pressnum(num):
    # 现将signflag和res设置为全局变量
    global signflag
    global res

    # 判断当前是否按下了运算符按钮
    if signflag == True :
        # 直接将界面设置为0
        val.set('0')
        # 并且将运算标志设置为False
        signflag = False

    # 判断当前显示面板显示的是否为运算结果
    if res == True :
        # 直接将界面设置为0
        val.set('0')
        # 并且将运算标志设置为False
        res = False

    # 判断按下数字时是否将当前按下的数字与原数字进行连接操作
    if(val.get() == '0') :
        # 将按得数字在面板中显示
        val.set(num)
    else :
        # 将按得数字在面板中显示
        val.set(val.get() + num)

# 运算序列
def presssign(sign):
    # 现将lists和signflag设置为全局变量
    global lists
    global signflag

    # 判断刚刚是否按下过运算符
    if signflag == True :
        # 将上一个运算符踢出列表
        lists.pop()
        # 将新的运算符加入到列表中
        lists.append(sign)
        print(lists)
    else :
        # 将面板中的数值进行存储
        lists.append(val.get())
        # 将运算符存起来
        lists.append(sign)
        print(lists)
        # 修改运算符标记状态
        signflag = True


# 等于
def pressdone():
    # 现将lists和res设置为全局变量
    global lists
    global res
    # 将面板上的数字加到lists中
    lists.append(val.get())

    # 进行运算 将列表转化为字符串
    strs = ''.join(lists)
    # 使用eval执行运算的字符串
    res = eval(strs)

    # 将运算的放入面板
    val.set(str(res))

    # 将结果显示标记设置为True
    res = True

    # 清空lists列表
    lists.clear()

# 界面布局
# 设置label的变量
val = StringVar()
val.set('0')
# 显示面板
label1 = Label(root,textvariable = val, bg='LightGray', font = ('黑体', 30), width=17, anchor = 'e').grid(row = 0, column = 0, columnspan = 4)

'''
为什么command这里调用函数的时候会调用lambda表达式(函数)
   1.因为command调用函数的语法格式中不需要在函数名的后面加(),所以没有办法往函数中传递参数。
   2.因为lambda表达式也是一个匿名函数，所以可以调用这个匿名函数，然后再通过lambda的调用自定义函数，并将参数传进去
'''

'''
第一排
'''
Button(root, text = 'C', width = 27, height = 2, command = clear).grid(row = 1, column = 0, columnspan = 3)
Button(root, text = '➗', width = 9, height = 2, command = lambda:presssign('/')).grid(row = 1, column = 3)

'''
第二排
'''
Button(root, text = 1, width = 9, height = 2, command = lambda:pressnum('1')).grid(row = 2,column = 0, padx = 0)
Button(root, text = 2, width = 9, height = 2, command = lambda:pressnum('2')).grid(row = 2,column = 1, padx = 0)
Button(root, text = 3, width = 9, height = 2, command = lambda:pressnum('3')).grid(row = 2,column = 2, padx = 0)
Button(root, text = '✖️', width = 9, height = 2, command = lambda:presssign('*')).grid(row = 2, column = 3)

'''
第三排
'''
Button(root, text = 4, width = 9, height = 2, command = lambda:pressnum('4')).grid(row = 3,column = 0, padx = 0)
Button(root, text = 5, width = 9, height = 2, command = lambda:pressnum('5')).grid(row = 3,column = 1, padx = 0)
Button(root, text = 6, width = 9, height = 2, command = lambda:pressnum('6')).grid(row = 3,column = 2, padx = 0)
Button(root, text = '➖', width = 9, height = 2, command = lambda:presssign('-')).grid(row = 3, column = 3)

'''
第四排
'''
Button(root, text = 7, width = 9, height = 2, command = lambda:pressnum('7')).grid(row = 4,column = 0, padx = 0)
Button(root, text = 8, width = 9, height = 2, command = lambda:pressnum('8')).grid(row = 4,column = 1, padx = 0)
Button(root, text = 9, width = 9, height = 2, command = lambda:pressnum('9')).grid(row = 4,column = 2, padx = 0)
Button(root, text = '➕', width = 9, height = 2, command = lambda:presssign('+')).grid(row = 4, column = 3)

'''
第五排
'''
Button(root, text = 0, width = 27, height = 2, command = lambda:pressnum('0')).grid(row = 5, column = 0, columnspan = 3)
Button(root, text = '=', width = 9, height = 2, command = pressdone).grid(row = 5, column = 3)

# 将窗口一直保持在消息循环的状态
root.mainloop()
