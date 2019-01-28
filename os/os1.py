#!/usr/bin/python3

import os

# getcwd 获取当前工作目录
# print(os.getcwd())

# chdir 修改当前工作目录
# os.chdir('/Users')

# listdir 获取指定文件夹中所有的文件和文件夹组成的列表
# print(os.listdir('/Users/smurfs'))

# mkdir 创建一个目录
# os.mkdir('one')

# makedirs 递归创建目录
# os.makedirs('one/two/thr')

# rmdir 移除一个目录
# os.rmdir('one')

# removedirs 递归删除目录
# os.removedirs('one/two/thr')

# rename 修改文件或文件夹的名称
# os.rename('test.txt','a.txt')

# stat 获取文件的相关信息
# print(os.stat('./a.txt'))

# system 执行系统命令
# os.system('ping www.baodi.com -c 3')

# getenv() 获取系统环境变量
# print(os.getenv('PATH'))

# abspath 将相对路径转换为绝对路径
# print(os.path.abspath('./'))

# splitext 将一个文件切割成名字和后缀两部分
# print(os.path.splitext('test.txt'))

# getsize 获取一个文件的大小
# print(os.path.getsize('one.py'))

# isdir 检测一个路径是否是目录
print(os.path.isdir('../test'))

# isfile 检测一个路径是否是文件
print(os.path.isfile('a.txt'))
