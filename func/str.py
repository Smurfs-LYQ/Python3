#!/usr/bin/python3
# 字符串操作与函数

'''
##########
#字符串操作
##########

# + 字符串连接操作
str1 = '一'
str2 = '二'
print(str1 + ',' + str2)

# * 字符串复制操作
str1 = '**********\n'
print(str1 * 5)

# [索引值] 字符串索引操作
str1 = 'abcdefghijklmnopqrstuvwxyz'
print(str1[0])

# [开始索引:结束索引:间隔值] 字符串取片操作
str1 = 'abcdefghijklmnopqrstuvwxyz'
print(str1[0:4])
str2 = '102030405060708090'
print(str2[0::2])

# r 元字符串，所有字符串中的转义字符不会转义，当做普通字符
str1 = r"123\r\n"
print(str1)
'''

######
#函数#
######

'''
# capitalize() 首字母大写
str1 = 'python'
print(str1.capitalize())

# title() 每个单词的首字母大写
str1 = 'python is best'
print(str1.title())

# upper() 所有字母变成大写
str1 = 'python'
print(str1.upper())

# lower() 将所有字母变为小写
str1 = 'PYTHON'
print(str1.lower())

# swapcase() 大小写转换
str1 = 'python IS best'
print(str1.swapcase())

# len() 计算长度
str1 = '用于计算长度'
print(len(str1))
list1 = ['one', 'two', 'thr']
print(len(list1))

# count() 计算指定字符出现的次数
str1 = '用于计算长度，用用用，长长'
print(str1.count('用'))
print(str1.count('用',6,10))
list1 = ['one', 'two', 'one']
print(list1.count('one'))

# find() 查找指定字符串第一次出现的位置
str1 = '用于计算长度，用用用，长长'
print(str1.find('长',6,13))

# index() 查找指定字符串第一次出现的位置
str1 = '用于计算长度，用用用，长长'
print(str1.index('长',6,13))

# startswith() 检测字符串是否以指定字符串开头
url = 'https://www.baidu.com'
print(url.startswith('https'))

# endswith() 检测字符串是否以指定字符串结尾
url = 'https://www.baidu.com'
print(url.endswith('com'))

# isupper() 检测字符串是否为全大写
str1 = 'ABC'
print(str1.isupper())

# islower() 检测字符串是否为全小写
str1 = 'abc'
print(str1.islower())

# isalnum() 检测字符串是否仅为字母和数字
str1 = '123abc测试'
print(str1.isalnum())

# isalpha() 检测字符串是否仅为字母
str1 = 'abc测试'
print(str1.isalpha())

# isdigit() 检测字符串是否仅为数字
str1 = '123'
print(str1.isdigit())

# isspace() 检测字符串是否为空白字符
str1 = '  '
print(str1.isspace())

# istitle() 检测字符串是否符合title()的结果
str1 = 'is best'
str1 = str1.title()
print(str1.istitle())

# isnumeric() 检测字符串是否是数值字符串
str1 = '123'
print(str1.isnumeric())

# isdecimal() 检测字符串是否是数值字符串
str1 = '123'
print(str1.isdecimal())

# split() 使用指定字符切割字符串
str1 = 'a1ab1abc'
print(str1.split('1'))

# splitlines() 将字符串在回车换行处进行切割
str1 = """
123
abc
一二三
"""
print(str1.splitlines())

# join() 将列表中的内容按照指定字符拼接成一个字符串
list1 = ['one', 'two', 'thr']
print(','.join(list1))

# zfill() 在原有字符串长度不足指定长度时，用0填充
str1 = '123'
print(str1.zfill(5))

# center() 指定字符串长度，并且使得源字符串居中，其余位置使用指定字符填充
str1 = '123'
print(str1.center(7))

# ljust() 指定字符串长度，如果不足会在字符串左边填充指定字符
str1 = '123'
print(str1.ljust(5,'!'))

# rjust() 指定字符串长度，如果不足会在字符串右边填充指定字符
str1 = '123'
print(str1.rjust(5,'!'))

# strip() 去掉字符串左右两侧的指定字符，默认为空格
str1 = '  123  '
print(str1.strip())

# lstrip() 去掉字符串左的指定字符，默认为空格
str1 = '..123..'
print(str1.lstrip('.'))

# rstrip() 去掉字符串右的指定字符，默认为空格
str1 = '..123..'
print(str1.rstrip('.'))

# 字符串替换
str1 = '124四6'
# maketrans() 建立字符串映射表
table = ''.maketrans('46','35')
# translate() 替换操作
print(str1.translate(table))

# ord 将ASCII码转换成字符串
print(ord('A'))

# chr 将字符串转换成ASCII码
print(chr(65))
'''
