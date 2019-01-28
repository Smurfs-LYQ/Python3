#!/usr/bin/python3

# 声明一个类
class DriveCar :
    # 成员属性
    driver = 'LYQ'
    car = '大众 CC 2018'
    people = '5'

    # 成员方法
    def go():
        return('开车方法')

    def stop():
        return('停车方法')

    # 对象可以调用的方法 self只用于接收对象
    def obj(self):
        return('对象可以调用的方法')

'''
# 对象和类的成员检测

# 检测类中所有的成员属性
print(DriveCar.__dict__)
# 调用类中的成员属性
print(DriveCar.driver)
'''

# 类成员操作

'''
# 访问类中的成员
# 属性
print(DriveCar.driver)
# 方法
print(DriveCar.go())

# 修改类中的成员
# 属性
DriveCar.people = '4'
print(DriveCar.people)
# 方法
DriveCar.stop = lambda : print('stop')
DriveCar.stop()

# 删除类中的成员
# 属性
del DriveCar.car
# 方法
del DriveCar.stop
print(DriveCar.__dict__)

# 添加类中的成员
# 属性
DriveCar.test = '123'
print(DriveCar.test)
# 方法
DriveCar.abc = lambda : print('abc')
DriveCar.abc()
'''

'''
# 对象的操作

# 实例化
dc = DriveCar()
# print(dc.obj())

# 访问对象中的成员
# 属性
print(dc.driver)
# 方法
print(dc.obj())

# 修改对象中的成员
# 属性
dc.people = 4
print(dc.people)
# 方法
dc.obj = lambda : print('obj')
dc.obj()

# 增加对象中的成员
# 属性
dc.one = 'one'
# 方法
dc.two = lambda : print('two')
print(dc.__dict__)

# 删除对象中的成员
# 属性
del dc.one
# 方法
del dc.two
print(dc.__dict__)
'''

'''
# 公共的封装
class Test_A :
    # 成员属性
    name = 'test_a'

    # 成员方法
    def go() :
        print('可以走')

# 子类继承父类
class Test_B(Test_A) :
    def one() :
        print('one')

print(Test_B.name)
Test_B.go()
'''

# 私有化封装
# 公共的封装
class TestA :
    # 成员属性
    __name = 'test_a'
    _age = '123'

    # 成员方法
    def __go(self) :
        print(TestA.__name)

    def _one() :
        return(TestA._age)

# print(TestA._TestA__name)
# TestA._TestA__go('')
# print(TestA._age)
# print(TestA._one())
# TestA.one()
Ta = TestA()
# print(Ta._TestA__name)
# Ta._TestA__go()
# print(Ta._age)
print(Ta._TestA__go())

# TestA.go()
# print(TestA.name)
# # 子类继承父类
# class Test_B(TestA) :
#     def one() :
#         print('one')
#
# print(Test_B.name)
# Test_B.go()
