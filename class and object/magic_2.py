#!/usr/bin/python3

##############################
#### 与属性操作相关的魔术方法 ####
##############################

# 定义一个类
class Person :

    # 成员属性
    name = 'test123'
    sex = '未知'
    age = '18'

    # 魔术方法
    """
    def __getattribute__(self,attrname) :
        '''
            触发时机：获取成员的时候被触发，无论成员是否存在
            参数：
                1. 一个用于接收对象的参数（self)
                2. 一个用于获取成员的名称
            返回值：必须有
            作用：在具有封装操作(私有化时)，为程序开部分访问权限使用
        '''
        print('调用了 __getattribute__ 魔术方法')
        if attrname == 'name' :
            return '123'
        else :
            return None
    """

    """
    def __getattr__(self,attrname) :
        '''
            触发时机：获取不存在的成员时被触发
            参数：
                1. 一个用于接收对象的参数（self)
                2. 一个用于获取成员的名称
            返回值：必须有
            作用：为访问不存在的属性设置值
        '''
        print('__getattr__ 被触发')
    """

    """
    def __setattr__(self,attrname,attrval) :
        '''
            触发时机：设置成员属性的值的时候被触发
            参数：
                1. 一个用于接收对象的参数（self)
                2. 被设置属性的名字
                3. 要设置的值
            返回值：无
            作用：接管设置操作，可以在设置之前进行判断行为操作
            注意：因为直接用self.attrname = attrval设置会导致无限
                递归，所以只能借助基本的object对象的设置方法代为操作
        '''
        print('__setattr__ 被触发')
        object.__setattr__(self,attrname,attrval)
    """

    """
    def __delattr__(self,attrname) :
        '''
            触发时机：删除属性的时候被触发
            参数：
                1. 一个用于接收对象的参数（self)
                2. 被属性属性的名字
            返回值：无
            作用：在删除一个属性的时候判断是否可以删除
            注意：因为直接用del self.attrname删除会导致无限递归，
                所以只能借助基本的object对象的设置方法代为操作
        '''
        if attrname == 'test' :
            object.__delattr__(self,attrname)
        else :
            pass
        print('__deleteattr__ 被触发')
    """

    def __dir__(self) :
        '''
            触发时机：当使用dir获取成员列表的时候被触发
            参数：
                1. 一个用于接收对象的参数（self)
            返回值：必须是列表
            作用：可以自定义返回的dir列表
        '''
        return ['one','two']

# 实例化对象
man = Person()

# 获取name的值
# print(man.name)

# 设置age的值
# man.age = '20'
# print(man.age)

# 删除sex的值
# man.test = '123'
# print(man.__dict__)
# del man.test
# print(man.__dict__)

man.name = 'name'
man.age = 'age'

print(dir(man))
