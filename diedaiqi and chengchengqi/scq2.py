#!/usr/bin/python3

#------------------------函数生成器------------------------#
# 大文件读取
def readbigfile(filepath) :

    # 每次读取的数据量
    every_size = 1

    # 打开文件
    with open(filepath,'r') as fp :
        # 循环读取数据,每次只读取一个G
        while True :
            # 一次读取指定大小的数据
            data = fp.read(every_size)

            # 判断是否有数据
            if len(data) > 0 :
                # 返回数据
                yield data
            else :
                return False

# 获取生成器
scq = readbigfile('./one.txt')

# 迭代生成器
for i in scq :
    print(i)
