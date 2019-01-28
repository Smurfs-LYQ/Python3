#!/usr/bin/python3

# 装饰器示例

"""
# 定义test函数的装饰器
def testzs(func) :
    # 这是未来的test函数(原参数有什么形参，这里就需要有什么形参)
    def _testzs(*one,**two) :
        print('描述符开始')
        res = func(*one,**two)
        print('描述符结束')
        return res

    return _testzs

# 语法糖
@testzs # 相当于 test = testzs(test)  调用了装饰器
# 定义一个普通的函数
# def test(one,two) :
def test(*one,**two) : # 收集参数，*代表列表 **代表元组
    print('test123')
    print(one)
    print(two)
    return '这是test函数'

print(test('1','一',tw1='2',tw2='二'))
"""

"""
# 装饰器带参数示例
def test(arg):
    def _test(func):
        def __testone():
            print('这是testone的描述符')
            res = func()
            return res

        def __testtwo():
            print('这是testtwo的描述符')
            res = func()
            return res

        if arg == 'o' :
            return __testone
        elif arg == 't' :
            return __testtwo
    return _test

# 语法糖
@test('o')
def one():
    print('函数one')
    return '函数1'

# 语法糖
@test('t')
def two():
    print('函数two')
    return '函数2'

print(one())
print('###################')
print(two())
"""

"""
# 将类作为装饰器参数传入进来
class Zs :
    # 绑定类的方法
    def Begin() :
        print('类开始')

    # 绑定类的方法
    def Down() :
        print('类结束')

def testzs(cls):
    def _testzs(func) :
        # 这是未来的test函数
        def __testzs():
            cls.Begin()
            res = func()
            cls.Down()
            return res
        # 返回装饰之后的函数
        return __testzs

    return _testzs

@testzs(Zs)
def test():
    print('test')
    return '函数test'

test()
"""

"""
# 把类作为装饰器使用
class testzs :
    # 此魔术方法用于接收原函数（被装饰的函数）
    def __call__(self,func):
        #将原函数存到对象当中
        self.func = func
        # 返回装饰之后的函数
        return self.zs

    # 装饰函数
    def zs(self):
        print('装饰开始')
        # 调用原函数
        res = self.func()
        print('装饰结束')
        return res

@testzs()
def test():
    print('test')
    return '函数test'

print(test())
"""

# 为类添加装饰器（单例模式）

# 为保存对象声明一个容器
obj = {}
# 声明装饰器
def testzs(cls) :
    def _zs() :
        if 'only' in obj :
            return obj['only']
        else :
            obj['only'] = cls()
            return obj['only']
    return _zs

# 语法糖
@testzs
# 定义一个类
class test :
    def one() :
        print('one方法')

a = test()
print(a)

b = test()
print(b)
