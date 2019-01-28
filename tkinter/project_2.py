#!/usr/bin/python3

# # from tkinter import *
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import zipfile
import os

# 创建tkinter主窗口
root = tkinter.Tk()

# 设置窗口的最小大小
root.minsize(300,300)

# 创建文件列表变量，用于在面板中显示面板信息
filelists = tkinter.StringVar()
filelists.set('没有文件信息')

# 声明添加文件的函数
def addfile() :
    # 全局化paths
    global paths

    # 打开选取文件的对话框
    paths = tkinter.filedialog.askopenfilenames(title = '请选择要压缩的文件')
    # 将元组变成字符串
    lists = '\n'.join(paths)
    # 将选中的文件添加到显示面板当中
    filelists.set(lists)

# 压缩文件操作
def compressfile() :
    # 全局化paths
    global paths

    # 弹出选择压缩地址路径的对话框
    zfpath = tkinter.filedialog.askdirectory(title = '请选择文件保存地址')

    # 创建zip文件
    zf = zipfile.ZipFile(zfpath+'/压缩文件.zip','w')
    # 压缩操作
    for path in paths :
        zf.write(path, os.path.basename(path))

    # 关闭压缩文件
    zf.close()

    # 弹出操作成功的界面
    tkinter.messagebox.showinfo('提示','压缩完成')

    # 清空文件列表面板的内容
    filelists.set('没有文件信息')

# 解压缩文件操作
def uncommpressfile() :
    # 选择文件
    paths = tkinter.filedialog.askopenfilenames(title = '请选择解压缩文件', filetypes = [('zip file','*.zip'),('gz file','*.tar.gz')])

    # 将元组变成字符串
    lists = '\n'.join(paths)

    # 将选择的文件路径添加到面板
    filelists.set(lists)

    # 选择解压的位置
    path = tkinter.filedialog.askdirectory(title = '请选择解压的地址')

    # 解压操作
    for i in paths :
        # 拿到解压文件
        zf = zipfile.ZipFile(i,'r')
        # 开始解压
        zf.extractall(path)
        # 关闭解压文件
        zf.close()

    # 提示解压完成
    tkinter.messagebox.showinfo('提示','解压完成')

    # 清空文件列表面板的内容
    filelists.set('')


# 添加文件按钮
tkinter.Button(root, text = '添加文件', command = addfile).grid(row = 0, column = 0, padx = 20, pady = 20)
# 压缩文件按钮
tkinter.Button(root, text = '压缩文件', command = compressfile).grid(row = 0, column = 1, padx = 20, pady = 20)
# 解压文件按钮
tkinter.Button(root, text = '解压文件', command = uncommpressfile).grid(row = 0, column = 2, padx = 20, pady = 20)

# 文件列表的面板
tkinter.Label(root, textvariable = filelists, bg = 'LightGray', width=35, anchor = 'w').grid(row = 1, column = 0, columnspan = 3)

# 将窗口一直保持在消息循环中
root.mainloop()
