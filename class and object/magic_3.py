#!/usr/bin/python3

class MyInt(int) :
    pass

    """
    # __add__ 重载父类的加法运算
    def __add__(self,other) :
        return int(self) + int(other)
        # return int(self) - int(other)
    """

    """
    # __sub__ 重载父类的减法运算
    def __sub__(self,other) :
        return int(self) - int(other)
        # return int(self) + int(other)
    """

    """
    # __mul__ 重载父类的乘法运算
    def __mul__(self,other) :
        return int(self) * int(other)
        # return int(self) / int(other)
    """

    """
    # __truediv__ 重载父类的除法运算
    def __truediv__(self,other) :
        return int(self) / int(other)
        # return int(self) * int(other)
    """

    """
    # __floordiv__ 重载父类的整数除法运算
    def __floordiv__(self,other) :
        return int(self) // int(other)
        # return int(self) + int(other)
        '''
            真除法和整数除法的区别：
                真除法就是正常的除法操作
                整数除法就是去除了结果的小数点，并且除不开的显示为0
        '''
    """

    """
    # __mod__ 重载父类的取余运算
    def __mod__(self,other) :
        return int(self) % int(other)
    """

    # __divmod__ 定义当被divmod()调用时的行为
    def __divmod__(self,other) :
        pass


val1 = MyInt(1)
val2 = MyInt(2)

"""
# 自定义类型加法操作
res = val1 + val2
print(res)
"""

"""
# 自定义类型减法操作
res = val1 - val2
print(res)
"""

"""
# 自定义类型乘法操作
res = val1 * val2
print(res)
"""

"""
# 自定义类型除法操作
res = val1 / val2
print(res)
"""

"""
# 自定义类型整数除法操作
res = val1 // val2
print(res)
"""

"""
# 自定义类型取余操作
res = val1 % val2
print(res)
"""
