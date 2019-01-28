#!/usr/bin/python3

'''
# issubclass() 检测一个类是不是另外一个类的子类
class One :
    pass

class Two(One) :
    pass

print(issubclass(Two,One))
'''

'''
# isinstance() 检测一个对象是不是指定类的对象
class One :
    pass

a = One()

print(isinstance(a,One))
'''

'''
# hasattr() 检测 对象/类 是否具有某个成员属性
class One :
    T1 = '123'

    def T2() :
        print('T2')

print(hasattr(One,'T1'))
print(hasattr(One,'T2'))
'''

'''
# getattr() 获取 对象/类 成员的值
class One :
    T1 = '123'

    def T2() :
        print('T2')

print(getattr(One,'T1'))
print(getattr(One,'T2'))
'''

'''
# setattr() 修改 对象/类 成员的值
class One :
    T1 = '123'

    def T2() :
        print('T2')

setattr(One,'T1','一二三')
print(One.T1)
'''

'''
# delattr() 删除 对象/类 成员的值
class One :
    T1 = '123'
    T3 = '3'

    def T2() :
        print('T2')

print(One.T3)
delattr(One,'T3')
print(One.T3)
'''

'''
# dir() 获取指定 对象/类 的成员列表
class One :
    T1 = '123'

    def T2() :
        print('T2')

print(dir(One))
'''


#################
#####内置属性#####
#################

"""
# 定义一个类
class Human :
    '''
        类的文档
    '''

    pass

# 查看内置属性
print(Human.__dict__)

# 查看类的文档
print(Human.__doc__)

# 检测模块的名称   类.__name__ 是获取当前类名，如果直接写__name__则是获取模块名
print(__name__)

# 获取类的继承列表中所有父类组成的元组
print(Human.__bases__)
"""

# class Person :
#     name = 'one'
#
#     def __delattr__(self,attrname) :
#         print('被触发')
#
# man = Person()
#
# man.a = '123'
# print(man.__dict__)
# del man.a
# print(man.__dict__)

# 反向运算
"""
class MyInt(int) :

    def __radd__(self,other) :
        return int(self) + int(other)

val = MyInt(9)
print(1 + val)
"""

# 增量赋值运算
class MyInt(int) :

    def __iadd__(self,other) :
        return int(self) + int(other)

val = MyInt(9)
val += 1
print(val)
