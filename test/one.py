#!/usr/bin/python3


# # nonlocal
# def one():
#     a = 123
#     print(a)
#     def one_1():
#         nonlocal a
#         a += 1
#         print(a)
#     one_1()
#
# one()

def can():
    a = 123
    print(a)
    def one() :
        nonlocal a
        a += 1
        print(a)
    one()
    print(a)
can()
print(a)

'''
# lambda
two = lambda x,y : x*y
print(two(1,2))
'''

'''
# global 全局变量
one = 123
one += 1
print(one)
def test() :
    global one
    one += 1
    print(one)

test()
print(one)
'''
