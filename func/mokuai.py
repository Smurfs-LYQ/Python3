#!/usr/bin/python3

##########
#字符串模块#
##########

'''
# 引用模块
import string

# 调用模块中的功能
print(string.ascii_letters)
'''

#########
#数学模块#
#########

import math
'''
# ceil() 数字向上取整
num = 8.3
print(math.ceil(num))

# floor() 数字向下取整
num = 8.3
print(math.floor(num))

# pow() 计算一个数值的n次方
num = 7
print(math.pow(num,3))
# 不过一般不用，因为可以像下面这样操作
print(num**3)

# sqrt() 开平方
num = 16
print(math.sqrt(num))

# fabs() 对一个数值获取其绝对值操作
num = -99.4
print(math.fabs(num))

# modf() 将一个浮点数拆成两部分
num = 3.131592653
print(math.modf(num))

# fsum() 将一个序列的数值进行相加求和
list1 = [1,2,1]
print(math.fsum(list1))

# sum() 将一个序列的数值进行相加求和
list1 = [1,2,1]
print(sum(list1))
'''

import random
'''
# random() 获取 0-1 之间的随机数
print(random.random())

# choice() 随机获取列表中的值
list1 = [1,2,3,4,5]
print(random.choice(list1))

# shuffle() 随机打乱序列
list1 = [1,2,3,4,5]
random.shuffle(list1)
print(list1)

# randrange() 获取指定范围内指定间隔的随机数
print(random.randrange(1,9))
print(random.randrange(2,8,2)) # 间隔数2

# uniform() 获取指定范围内的随机数(小数)
print(random.uniform(1,9))
'''
