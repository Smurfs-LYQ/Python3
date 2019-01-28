#!/usr/bin/python3

##################
# 列表的遍历操作 #
##################
'''
# 一级列表的遍历
list1 = [1,2,3,4]

# for in
for i in list1 :
    print(i)
print(id(list1))

# while
i = 0
while i < len(list1):
	print(list1[i])
	i += 1
'''

'''
# 二级列表的遍历 one
list1 = [
	[1,2],
	['一','二'],
	['one','two']
]
for i,n in list1:
	print(i, end = '|')
	print(n)

# 二级列表的遍历 two
list1 = [[1],[1,2],[2],[2,3]]

# for
for i in list1 :
	for n in i :
		print(n,end=' ')
	print('')

# while
i = 0
while i < len(list1):
	#print(list1[i])
	n = 0
	while n < len(list1[i]):
		print(list1[i][n], end = ' ')
		n += 1	
	print(' ')
	i += 1
'''


######################################
# list content -> 列表内涵|列表推导式#
######################################
"""
# 简单的列表推导式
'''
普通的列表推导式：
	格式：[变量 for 变量 in 列表]
	作用：遍历列表中的每个值，并组成新的列表，可以对获取的值进行操作
带判断的列表推导式：
	格式：[变量 for 变量 in 列表 if 判断表达式]
	作用：遍历列表中的每个值，根据判断条件决定是否取出指定的值并组成新的列表，可以对获取的值进行操作
'''
list1 = ['一', '二', '三']
one = ['<'+i+'>' for i in list1]
print(one)

# 带有判断条件的列表推导式
list1 = [1,2,3,4,5,11,21,31,41,51]
one = [i for i in list1 if i < 10]
print(one)

# 多个列表推导式
'''
多个列表的同时循环的列表推导式：
	格式：[变量1+变量2 for 变量1 in 列表1 for 变量2 in 列表2]
	作用：遍历每个列表中的每个值，并组成新的列表，可以对获取的值进行操作
带判断的多个列表的同时循环的列表推导式：
	格式：[变量1+变量2 for 变量1 in 列表1 for 变量2 in 列表2 if 判断表达式]
	作用：遍历每个列表中的每个值，根据判断条件决定是否取出指定的值并组成新的列表，可以对获取的值进行操作

注意：
	变量1和变量2可以进行其他操作，不一定非要+，这只是个demo
	这里多个列表推到式都只能用同类型的列表 比如都是字符串类型
'''
list1 = ['一','二','三']
list2 = ['one','two','thr']

one = [i + '->' + n for i in list1 for n in list2]

print(one)

# 带有判断的多个列表推导式 one
num1 = [2,4,6,8]
num2 = [4,16,36,64]
one = [i + n for i in num1 for n in num2 if n == i*i]
print(one) 

# 带有判断的多个列表推导式 two
list1 = ['一','二','三']
list2 = ['one','two','thr']
one = [ x + '->' + y for x in list1 for y in list2 if list1.index(x) == list2.index(y)]
for i in one :
	print(i)
"""

############
# 列表函数 #
############

# append() 向列表末尾添加新元素
list1 = [1,2,3]
list1.append(4)
print(list1)

# clear() 清空列表
list1 = [1,2,3]
list1.clear()
print(list1)

# copy() 复制列表
list1 = [1,2,3]
list2 = list1.copy()
print(list2)
	
# count() 统计列表中指定元素出现的次数
list1 = [1,2,1]
print(list1.count(1))

# extend() 将一个列表继承另一个列表
list1 = [1,2,3]
list2 = ['一', '二', '三']
list1.extend(list2)
print(list1)

# insert() 在指定位置之前插入值
list1 = [1,2,3]
list1.insert(0,0)
print(list1)

# pop() 移除列表中的最后一个元素
list1 = [1,2,3,5]
list1.pop()
print(list1)

# remove() 移除列表中指定的值
list1 = [1,2,3,5]
list1.remove(5)
print(list1)

#reverse() 列表反转
list1 = [1,2,3]
list1.reverse()
print(list1)

# sort() 列表排序
list1 = [1,4,2,5,3]
list1.sort()             # 升序
list1.sort(reverse=True) # 降序
print(list1)







































