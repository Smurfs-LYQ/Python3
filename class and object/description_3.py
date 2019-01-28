#!/usr/bin/python3

#####################
########修饰符########
#####################

# 定义一个Email类
class Email :

    # 成员属性
    username = ''
    # 为描述符添加一个临时变量(在描述符中代替username进行操作,因为如果不这样会造成递归循环)
    _username = None
    password = ''

    # 成员方法
    # 处理username的获取操作
    @property
    def username(self):
        print('获取操作被触发')
        return self._username

    # 处理username的设置操作
    @username.setter
    def username(self,val):
        print('设置操作被触发')
        self._username = val

    # 处理username的删除操作
    @username.deleter
    def username(self):
        print('删除操作被触发')
        del self._username

# 实例化对象
email = Email()

# 设置操作
email.username = 'test'

# 获取操作
print(email.username)

# 删除操作
del email.username
print(email.username)
