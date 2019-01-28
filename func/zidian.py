#!/usr/bin/python3

# for 循环
'''
dict1 = {'one':1, 'two':2, 'thr':3}
for i in dict1 :
    print(dict1[i])

for i,n in dict1.items() :
    print(i, end='=')
    print(n)
'''

'''
# dict content 字典推导式
# 普通字典推导式
dict1 = {'one':1, 'two':2, 'thr':3}
res = {k+'=>':v for k,v in dict1.items()}
print(res)

# 带判断的字典推导式
dict1 = {'one':1, 'two':'2', 'thr':3}
res = {k:v for k,v in dict1.items() if type(v) != str}
print(res)

# 多个字典的字典推导式
dict1 = {'one':'1', 'two':'2', 'thr':'3'}
dict2 = {'AK':'7.62', 'M4':'5.56', 'AWM':'马格南'}
res = {i+x : n+y for i,n in dict1.items() for x,y in dict2.items()}
print(res)

# 带判断的多个字典的字典推导式
dict1 = {'one':'1', 'two':'2', 'thr':'3'}
dict2 = {'AK':'7.62', 'M4':'5.56', 'AWM':'马格南'}
res = {i+x : n+y for i,n in dict1.items() for x,y in dict2.items() if len(i) != len(y)}
print(res)
'''

# 字典函数
# clear() 清空字典
dict1 = {'one':1, 'two':2, 'thr':3}
dict1.clear()
print(dict1)

# copy() 复制字典
dict1 = {'one':1, 'two':2, 'thr':3}
dict2 = dict1.copy()
print(dict2)

# fromkeys() 将指定的一个序列当做键，剩下的一个值当做值
list1 = ['one', 'two', 'thr']
res = {}.fromkeys(list1, '值')
print(res)

# get() 获取指定键的值，如果没有这个键默认返回None
dict1 = {'one':'1', 'two':'2', 'thr':'3'}
print(dict1.get('t','可设置的返回值'))
dict1.pop('one')
print(dict1)

# popitem() 移除字典中的最后一个元素
dict1 = {'one':'1', 'two':'2', 'thr':'3'}
res = dict1.popitem()
print(dict1)
print(res)

# setdefault() 添加新的元素
dict1 = {'one':'1', 'two':'2', 'thr':'3'}
dict1.setdefault('test','test_one')
print(dict1)

# update() 通过键修改元素的内容
dict1 = {'one':'1', 'two':'2', 'thr':'3'}
dict1.update(thr='三')
dict1.update({'one':'一'})
print(dict1)
