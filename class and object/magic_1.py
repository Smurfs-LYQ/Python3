#!/usr/bin/python3

# 定义一个类
class Magic :

    # 成员属性
    T1 = '锤子T1'

    # 魔术方法

    """
    # __init__ 初始化魔术方法
    def __init__(self):
        '''
            触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）
            参数：至少有一个用于接收对象的参数（self)
            返回值：无
            作用：初始化对象的成员
            注意：使用该方法初始化的成员都是直接写入对象当中，类中无法具有
        '''
        print('初始化魔术方法被触发')
    """

    """
    # __new__ 实例化魔术方法
    def __new__(cls):
        '''
            触发时机：实例化对象的时候触发
            参数：至少一个cls 接收当前类
            返回值：必须返回一个对象实例
            作用：实例化对象
            注意：实例化对象是object类底层实现，其他类继承了object的__new__才能实例化对象
        '''
        print('实例化魔术方法被触发')

        # 返回一个实例化以后的对象（我们无法实现，借助底层实现）
        return object.__new__(cls);
    """

    """
    # __del__ 析构魔术方法
    def __del__(self):
        '''
            触发时机：对象无用时/对象被删除时被触发
            参数：至少有一个用于接收对象的参数（self)
            返回值：无
            作用：使用完对象时回收资源
        '''
        print('析构魔术方法被触发')
        # 将当前对象的成员进行释放,比如在打开文件操作后，此处关闭文件
    """

    """
    # __call__ 调用对象的魔术方法
    def __call__(self):
        '''
            触发时机：将对象当做函数调用时被触发 对象名()
            参数：至少有一个用于接收对象的参数（self)
            返回值：根据情况而定
            作用：可以将复杂的步骤进行合并操作
        '''
        print('调用对象的魔术方法被触发')
    """

    """
    # __len__ 调用len()函数的时候触发
    def __len__(self) :
        print('len魔术方法被触发')

        # 获取当前对象的所有成员 并 统计放回
        return(len(self.__dict__))

        '''
            触发时机：调用len()函数的时候触发
            参数：至少有一个用于接收对象的参数（self)
            返回值：必须返回一个整形
            作用：可以设置为检测对象成员个数，但是也可以进行其他任意操作
            注意：返回值必须是整数（格式要求，不然会报错）
        '''
    """

    """
    # __str__ 把一个对象当字符串使用的时候触发
    def __str__(self) :
        print('__str__ 魔术方法被触发')
        return '你打印对象干嘛'

        '''
            触发时机：把一个对象当字符串使用的时候触发
            参数：至少有一个用于接收对象的参数（self)
            返回值：必须返回一个字符串
            作用：里面的操作随你
        '''
    """

    """
    # __repr__ 调用repr()函数的时候被触发
    def __repr__(self) :
        print('__repr__函数被触发')
        return '字符串'

        '''
            触发时机：调用repr()函数的时候触发
            参数：至少有一个用于接收对象的参数（self)
            返回值：必须返回一个字符串
            作用：将对象使用repr转换成字符串时使用,可用于快捷操作
        '''
    """

    """
    # __bool__ 使用bool(对象)的时候被触发
    def __bool__(self) :
        print('__bool__ 魔术方法被触发')
        return True

        '''
            触发时机：使用bool(对象)的时候被触发
            参数：至少有一个用于接收对象的参数（self)
            返回值：必须是布尔值
            作用：根据实际情况决定，可以作为快捷方式使用
            注意：仅适合于返回布尔值的操作
        '''
    """

    # __format__ 想把对象格式化(format函数)的时候被触发
    def __format__(self,flag) :
        print(flag)

        return '__format__ 魔术方法被触发'
        '''
            触发时机：使用 字符串.format(对象) 的时候触发
            参数：一个用于接收对象的参数（self)，一个用于接收format的{}中的格式
            返回值：必须是字符串
            作用：设置对象可以作为format的参数，并且可以自定义对象格式化的规则
        '''

# 实例化对象
magic = Magic()
print('###{:格式随意}###'.format(magic))
