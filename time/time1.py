#!/usr/bin/python3

import time

# time 获取当前时间戳
# print(time.time())

# localtime 获取当前时间元组
# print(time.localtime())

# gmtime 获取当前UTC时间元祖
# print(time.gmtime())

# ctime 获取本地时间的字符串格式
# print(time.ctime())

# mktime 使用时间元组制作时间戳
# print(time.mktime((1971,1,1,0,0,0,0,0,0)))

# clock 获取CPU时间，用于计算代码执行时间
# 开始时间
# start = time.clock()
#
# time.sleep(1)
#
# # 结束时间
# end = time.clock()
#
# print(end - start)

# strftime 格式化输出时间字符串
print(time.strftime('%Y-%m-%d %H:%M:%S'))

# strptime 解析时间字符串成一个元组
print(time.strptime('2018-09-28 10:49:45','%Y-%m-%d %H:%M:%S'))
