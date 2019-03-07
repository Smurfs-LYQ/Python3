#!/usr/bin/python3

# 包含迭代器的类
class DDQ:

    # 初始化魔术方法
    def __init__(self) :
        # 添加一个计数成员/初始值
        self.index = 0

    # 可迭代协议(如果不加可迭代协议，就只能进行手动迭代)
    def __iter__(self) :
        # 返回迭代器所在的对象
        return self

    # 迭代器协议(实现了迭代器的魔术方法)
    def __next__(self) :
        # 获取当前的索引值
        i = self.index
        if i < 10 :
            # 将索引值+1
            self.index += 1

            # 一次迭代之后的返回
            return i
        else :
            # 停止迭代(抛出迭代终止异常对象) 注意这里不是return
            raise StopIteration

# 实例化对象
res = DDQ()

# 迭代操作
# 手动
'''
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
'''

# 自动
for i in res :
    print(i)
