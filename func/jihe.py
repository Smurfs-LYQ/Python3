#!/usr/bin/python3

# 创建空集合
set1 = set()
# print(type(set1))
# print(set1)

# 创建多个元素的集合
set1 = {1,2,3,3} # 重复的元素会被剔除掉
# print(type(set1))
# print(set1)

# 普通序列的遍历
set1 = {'one','two','thr'}
# for i in set1 :
    # print(i)

# 多级集合的遍历
set1 = {('one','two'),(1,2),('一','二')}
# for x,y in set1 :
    # print(x)
    # print(y)

# 单个集合的推导式
set1 = {'one','two','thr'}
# res = {i for i in set1}
# print(res)

# 带判断
set1 = {'one','two','thr',1,2,3}
# res = {i for i in set1 if type(i) == int}
# print(res)

# 多个集合的推导式
set1 = {'one','two','thr'}
set2 = {'一','二','三'}
# res = {x+y for x in set1 for y in set2}
# print(res)

# 带判断的多个集合推导式
set1 = {'1','two','3'}
set2 = {'一','二','三'}
# res = {x+y for x in set1 for y in set2 if len(x) == len(y)}
# print(res)


# 函数

# add 添加一个元素
set1 = {'two'}
# set1.add('one')
# print(set1)

# pop 删除元素
set2 = {'一','二','三'}
# set2.pop()
# print(set2)

# remove 删除元素
set2 = {'一','二','三'}
set2.remove('二')
print(set2)
