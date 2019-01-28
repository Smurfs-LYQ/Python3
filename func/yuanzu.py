#!/usr/bin/python3

##################################
# 元组和列表的循环体遍历方式一样 #
#   元组和列表的访问方式也一样   #
#   元组相较于列表不支持增删改   #
##################################

# tuple() 将其他数据类型转化为元组
'''
list1 = [1,2,3]
print(type(list1))
tuple1 = tuple(list1)
print(type(tuple1))
'''

'''
生成器和迭代器的区别
迭代器就好比是把一个序列提前做好了，随时用随时拿，比较占用系统资源
生成器就好比是把一个序列做成半成品，随时用随时调，比较节省系统资源
生成器是按需进行数据操作，大数据文件遍历的时候比较有优势
'''


#############
# 元组推导式 #
#############
'''
# 单个元组的元组推导式
tuple1 = ('一','二','三','四','五')
res = (i for i in tuple1) # 得到的是一个生成器，不像列表直接得到一个新列表
print(res)
# 遍历一个元组推导式得到的生成器
for i in res :
    print(i)

# 带有条件判断的单个元祖的元组推导式
tuple1 = ('一','二','三','四','五',1,2,3,4,5)
res = (i for i in tuple1 if type(i) == str)
for i in res :
    print(i)

# 多个元组的元组推导式
tuple1 = ('一','二','三','四','五')
tuple2 = ('1','2','3','4','5')
res = (x+'->'+y for x in tuple1 for y in tuple2)
print(res)
for i in res :
    print(i)

# 带有条件判断的多个元祖的元组推导式
tuple1 = ('一','二','三','四','五')
tuple2 = ('1','2','3','4','5')
res = (x + '=>' + y for x in tuple1 for y in tuple2 if tuple1.index(x) == tuple2.index(y))
for i in res :
    print(i)
'''

tuple1 = ('1','2','3','4','5','6','7','8','9')

# one
res = (y+'x'+x+'='+str(int(y)*int(x)) for x in tuple1 for y in tuple1 if tuple1.index(x) >= tuple1.index(y))
for i in res :
    print(i)

'''
# two
for i in tuple1 :
    res = (x for x in tuple1 if tuple1.index(i) >= tuple1.index(x))
    for n in res:
        one = int(n) * int(i)
        one = n + 'x' + i + '=' + str(one)
        print(one,end = ' ')
    print('')
'''
