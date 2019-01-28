#!/usr/bin/python3

#####################
########描述符########
#####################

# 声明一个邮件类
class Email :
    # 成员属性
    # 为描述符添加一个临时变量(在描述符中代替username进行操作,因为如果不这样会造成递归循环)
    _username = None
    password = ''

    # 成员方法

    # 获取username的描述符方法
    def fget(self): #self是类对象本身
        print('获取发放被触发')
        return self._username

    # 设置username的描述符方法
    def fset(self,val): #self是类对象本身 val是设置的值
        print('设置方法被触发')
        self._username = val

    # 删除username的描述符方法
    def fdel(self): #self是类对象本身
        print('删除方法被触发')
        del self._username

    # 为username成员属性添加描述符
    username = property(fget,fset,fdel)

# 实例化对象
email = Email()

# 设置username
email.username = '123'

# 获取username
print(email.username)

# 删除username
del email.username
print(email.username)
