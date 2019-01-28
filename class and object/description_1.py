#!/usr/bin/python3

#####################
########描述符########
#####################

# 定义描述符类
class Description :
    # 初始化魔术方法
    def __init__(self) :
        # 为当前类/对象添加一个成员属性来接收需要描述的成员属性 此处还没有接收(占位)
        self.name = ''

    '''
        self 用于接收当前描述符类的对象
        obj  用于接收管理成员的对象
    '''

    # 设置属性值的方法
    def __set__(self,obj,val):
        print('设置方法被触发')
        self.name = val

    # 获取属性值的方法
    def __get__(self,obj,cls) :
        print('获取方法被触发')
        return self.name

    # 删除属性值的方法
    def __delete__(self,obj):
        print('删除方法被触发')
        # 代为删除操作 如果不代为删除,那么只是执行了此方法而已,实际并没有删除
        del self.name

# 定义一个邮件类
class Email :
    # 属性
    site = Description()

# 实例化对象
email = Email()

# 测试描述符类设置值的方法
email.site = 'aaa123'

# 测试描述符类获取值的方法
print(email.site)

# 测试描述符类删除值的方法
del email.site
print(email.site)
