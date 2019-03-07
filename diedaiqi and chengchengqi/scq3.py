#!/usr/bin/python3

# send对于生成器的作用是修改生成器中指定元素的值
def scq() :
    i = 1

    while True :
        # 这是用于接收send发送过来值的固定格式
        num = (yield i)

        # 检测用户是否发送值过来
        if num is not None :
            i = num
        else :
            i += 1

res = scq()

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

# 修改生成器的值
res.send(10)

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
