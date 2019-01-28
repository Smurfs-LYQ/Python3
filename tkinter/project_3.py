#!/usr/bin/python3

from tkinter import *

class clac :
    # 初始化操作界面
    def __init__(self) :
        # 创建主窗口
        root = Tk()
        self.root = root

        # 定义主窗口名称
        self.root.title('Python面向对象计算器')

        # 设置主窗口最小大小
        self.root.minsize(300,210)

        # 定义面板的显示变量，并将它存入对象当中
        self.val = StringVar()
        self.val.set('0')
        # 存储当前操作步骤
        self.lists = []
        # 标记当前是否按下了运算符按钮
        self.signflag = False
        # 标记当前显示的是否为运算结果
        self.res = False

        # 调用显示面板
        self.show()

        # 调用按钮
        self.but()

        # 将窗口一直保存在消息循环的状态
        root.mainloop()

    # 定义显示面板
    def show(self) :
        Label(self.root, textvariable = self.val, bg='LightGray', font = ('黑体', 30), width=17, anchor = 'e').grid(row = 0, column = 0, columnspan = 4)

    # 定义按钮布局
    def but(self) :
        # 第一排
        Button(self.root, text = 'C', width = 27, height = 2, command = self.clear).grid(row = 1, column = 0, columnspan = 3)
        Button(self.root, text = '➗', width = 9, height = 2, command = lambda:self.presssign('/')).grid(row = 1, column = 3)

        # 第二排
        Button(self.root, text = 1, width = 9, height = 2, command = lambda:self.pressnum('1')).grid(row = 2,column = 0, padx = 0)
        Button(self.root, text = 2, width = 9, height = 2, command = lambda:self.pressnum('2')).grid(row = 2,column = 1, padx = 0)
        Button(self.root, text = 3, width = 9, height = 2, command = lambda:self.pressnum('3')).grid(row = 2,column = 2, padx = 0)
        Button(self.root, text = '✖️', width = 9, height = 2, command = lambda:self.presssign('*')).grid(row = 2, column = 3)

        # 第三排
        Button(self.root, text = 4, width = 9, height = 2, command = lambda:self.pressnum('4')).grid(row = 3,column = 0, padx = 0)
        Button(self.root, text = 5, width = 9, height = 2, command = lambda:self.pressnum('5')).grid(row = 3,column = 1, padx = 0)
        Button(self.root, text = 6, width = 9, height = 2, command = lambda:self.pressnum('6')).grid(row = 3,column = 2, padx = 0)
        Button(self.root, text = '➖', width = 9, height = 2, command = lambda:self.presssign('-')).grid(row = 3, column = 3)

        # 第四排
        Button(self.root, text = 7, width = 9, height = 2, command = lambda:self.pressnum('7')).grid(row = 4,column = 0, padx = 0)
        Button(self.root, text = 8, width = 9, height = 2, command = lambda:self.pressnum('8')).grid(row = 4,column = 1, padx = 0)
        Button(self.root, text = 9, width = 9, height = 2, command = lambda:self.pressnum('9')).grid(row = 4,column = 2, padx = 0)
        Button(self.root, text = '➕', width = 9, height = 2, command = lambda:self.presssign('+')).grid(row = 4, column = 3)

        # 第五排
        Button(self.root, text = 0, width = 27, height = 2, command = lambda:self.pressnum('0')).grid(row = 5, column = 0, columnspan = 3)
        Button(self.root, text = '=', width = 9, height = 2, command = self.pressdone).grid(row = 5, column = 3)

    # 定义清空操作
    def clear(self) :
        self.val.set('0')

    # 数字按钮操作
    def pressnum(self,num):
        # 判断当前是否按下了运算符按钮
        if self.signflag == True :
            # 直接将界面设置为0
            self.val.set('0')
            # 并且将运算标志设置为False
            self.signflag = False

        # 判断当前显示面板显示的是否为运算结果
        if self.res == True :
            # 直接将界面设置为0
            self.val.set('0')
            # 并且将运算标志设置为False
            self.res = False

        # 判断按下数字时是否将当前按下的数字与原数字进行连接操作
        if(self.val.get() == '0') :
            # 将按得数字在面板中显示
            self.val.set(num)
        else :
            # 将按得数字在面板中显示
            self.val.set(self.val.get() + num)

    # 运算序列
    def presssign(self,sign):
        # 判断刚刚是否按下过运算符
        if self.signflag == True :
            # 将上一个运算符踢出列表
            self.lists.pop()
            # 将新的运算符加入到列表中
            self.lists.append(sign)
            print(self.lists)
        else :
            # 将面板中的数值进行存储
            self.lists.append(self.val.get())
            # 将运算符存起来
            self.lists.append(sign)
            print(self.lists)
            # 修改运算符标记状态
            self.signflag = True


    # 等于
    def pressdone(self):
        # 将面板上的数字加到lists中
        self.lists.append(self.val.get())

        # 进行运算 将列表转化为字符串
        strs = ''.join(self.lists)
        # 使用eval执行运算的字符串
        self.res = eval(strs)

        # 将运算的放入面板
        self.val.set(str(self.res))

        # 将结果显示标记设置为True
        self.res = True

        # 清空lists列表
        self.lists.clear()

obj = clac()
