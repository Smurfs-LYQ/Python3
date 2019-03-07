#!/usr/bin/python3

# 元组推导式的结果就是制作一个生成器，生成器的结果就是一个对象
'''
scq = (i for i in range(1,10))

for i in scq :
    print(i)
'''

# 生成器函数
def scq() :
    # yield
    #   他的作用是将yield后面的值返回给next迭代器
    yield 1
    yield 3
    yield 5
    yield 7
    yield 9

# 获取生成器
a = scq()

# 手动调用生成器
print(next(a))

# 自动调用生成器
for i in a :
    if i == 5 :
        # 提前关闭生成器(生成器没有结束时一直等待调用，close让他关闭)
        a.close()
    print(i)
